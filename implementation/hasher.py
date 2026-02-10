import hashlib

def generate_hash(file_storage):
    """
    Generates a SHA-256 hash for a Flask FileStorage object.
    """
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Read the file in chunks to handle large files (like your Oracle certificate)
    # Seek to start to ensure we read from the beginning
    file_storage.seek(0)
    for byte_block in iter(lambda: file_storage.read(4096), b""):
        sha256_hash.update(byte_block)
    
    # Reset file pointer so other functions can read it if needed
    file_storage.seek(0)
    
    # Return the 64-character hexadecimal string
    return sha256_hash.hexdigest()