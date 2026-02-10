from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def cbc_demo():
    key = os.urandom(16)
    iv = os.urandom(16)
    plaintext = b"BLOCK_NUMBER_ONE_BLOCK_NUMBER_TWO_BLOCK_NUMBER_THRE" # 51 bytes
    
    # 1. ADD PADDING
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 2. ENCRYPTION (Now it won't crash!)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 3. INTRODUCE ERROR (Flip a bit in C1)
    corrupted_ct = bytearray(ciphertext)
    corrupted_ct[0] ^= 0xFF 
    
    # 4. DECRYPTION
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(corrupted_ct) + decryptor.finalize()
    
    # 5. REMOVE PADDING (Handle error if padding is corrupted)
    try:
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
        print("Decryption successful (with errors in text).")
    except:
        print("Warning: Padding was corrupted, showing raw decrypted blocks instead.")
        decrypted = decrypted_padded

    # Check first few bytes to see the corruption
    print(f"Original:  {plaintext[:20]}...")
    print(f"Decrypted: {decrypted[:20]}...")

cbc_demo()