from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def triple_des_cbc_demo():
    # 3DES requires a 24-byte key (192 bits)
    key = os.urandom(24)
    # The block size for 3DES is 8 bytes (64 bits)
    iv = os.urandom(8)
    
    plaintext = b"This is a secret message using 3DES CBC mode."

    # 1. Padding: 3DES has an 8-byte block size (64 bits)
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # 2. Encryption
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # 3. Decryption
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
    # 4. Unpadding
    unpadder = padding.PKCS7(64).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    print(f"Algorithm: 3DES")
    print(f"Ciphertext (hex): {ciphertext.hex()[:40]}...")
    print(f"Decrypted Text: {decrypted.decode()}")

triple_des_cbc_demo()