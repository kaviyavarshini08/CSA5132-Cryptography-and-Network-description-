from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def pad(data, block_size):
    
    padding_len = block_size - (len(data) % block_size)
    padding = b'\x80' + b'\x00' * (padding_len - 1)
    return data + padding

def encrypt_message(mode_name, key, iv, plaintext):
    block_size = 16 # AES block size is 128 bits (16 bytes)
    padded_data = pad(plaintext, block_size)
    
    # Select Mode
    if mode_name == "ECB":
        mode = modes.ECB()
    elif mode_name == "CBC":
        mode = modes.CBC(iv)
    elif mode_name == "CFB":
        mode = modes.CFB(iv)
    
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data) + encryptor.finalize()

# --- Execution ---
key = os.urandom(32)  # AES-256
iv = os.urandom(16)   # Initialization Vector
message = b"Hello! This is a secret message." # 32 bytes (exactly 2 blocks)

print(f"Original Length: {len(message)} bytes")

for mode in ["ECB", "CBC", "CFB"]:
    ciphertext = encrypt_message(mode, key, iv, message)
    print(f"{mode} Ciphertext (hex): {ciphertext.hex()[:40]}... (Length: {len(ciphertext)})")