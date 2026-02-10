from flask import Flask, render_template, request, redirect, url_for, session
import database
import hasher

app = Flask(__name__)

# This key encrypts your login session so it's secure
app.secret_key = 'secured_doc_2026_key_secret'

# Admin Credentials for your project demo
ADMIN_USER = "admin"
ADMIN_PASS = "secure123"

@app.route('/')
def index():
    """Renders the high-end Home/Login page."""
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Handles the authentication logic."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == ADMIN_USER and password == ADMIN_PASS:
        session['logged_in'] = True
        return redirect(url_for('issue_page'))
    else:
        # If login fails, go back to home with an error message
        return render_template('index.html', error="Invalid Credentials")

@app.route('/issue')
def issue_page():
    """Only accessible if the user is logged in."""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('issue.html')

@app.route('/verify')
def verify_page():
    """Publicly accessible verification portal."""
    return render_template('verify.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles the document registration process."""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    
    name = request.form['name']
    id_no = request.form['roll']
    doc_type = request.form.get('doc_type', 'General')
    file = request.files['certificate']
    
    if file:
        file_hash = hasher.generate_hash(file)
        database.save_certificate(name, id_no, file_hash, doc_type)
        return render_template('result.html', 
                             status="success", 
                             message=f"Credential for {name} registered!", 
                             hash_val=file_hash)

@app.route('/check', methods=['POST'])
def check_file():
    """Public verification logic."""
    file = request.files['certificate']
    if file:
        file_hash = hasher.generate_hash(file)
        result = database.find_certificate(file_hash)
        if result:
            return render_template('result.html', 
                                 status="verified", 
                                 name=result.get('name'), 
                                 roll=result.get('roll'), 
                                 doc_type=result.get('doc_type'), 
                                 hash_val=file_hash)
        else:
            return render_template('result.html', status="tampered")

@app.route('/logout')
def logout():
    """Logs the admin out and clears the session."""
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)