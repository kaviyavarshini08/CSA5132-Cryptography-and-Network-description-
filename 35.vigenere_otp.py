
# File Name: vigenere_otp.py
import random

def vigenere_otp(text, key=None):
    text = text.upper().replace(" ", "")
    # Generate a random key if one isn't provided
    if key is None:
        key = [random.randint(0, 25) for _ in range(len(text))]
    
    cipher_text = ""
    for i in range(len(text)):
        # Shift character by the corresponding key value
        p = ord(text[i]) - ord('A')
        c = (p + key[i]) % 26
        cipher_text += chr(c + ord('A'))
        
    return cipher_text, key

# Example Usage
msg = "HELLO"
encrypted, key_used = vigenere_otp(msg)
print(f"Plaintext:  {msg}")
print(f"Key Stream: {key_used}")
print(f"Ciphertext: {encrypted}")
