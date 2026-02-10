from pymongo import MongoClient

# Initialize the MongoDB Client
# Ensure MongoDB Compass is running and connected to localhost:27017
client = MongoClient("mongodb://localhost:27017/")
db = client["SecuredDocDB"]
collection = db["certificates"]

def save_certificate(name, roll, file_hash, doc_type):
    """
    Saves the credential metadata and SHA-256 hash into MongoDB.
    Accepts 4 parameters to support universal document categories.
    """
    document = {
        "name": name,
        "roll": roll,  # Unique Identification Number
        "hash": file_hash,
        "doc_type": doc_type  # The new 'Document Category' attribute
    }
    
    # Use update_one with upsert=True to prevent duplicate hash entries
    collection.update_one(
        {"hash": file_hash}, 
        {"$set": document}, 
        upsert=True
    )
    print(f"DEBUG: Successfully secured document for {name} in MongoDB.")

def find_certificate(file_hash):
    """
    Searches the database for a matching SHA-256 hash.
    Returns the full document if found, otherwise returns None.
    """
    result = collection.find_one({"hash": file_hash})
    return result