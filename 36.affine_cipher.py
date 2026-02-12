# File Name: affine_cipher.py
import math

def is_valid_key(a):
    # 'a' must be coprime to 26
    return math.gcd(a, 26) == 1

def affine_encrypt(text, a, b):
    if not is_valid_key(a):
        return f"Error: 'a={a}' is not valid (must be coprime to 26)."
    
    result = ""
    for char in text.upper():
        if char.isalpha():
            # p = character index (0-25)
            p = ord(char) - ord('A')
            # C = (ap + b) mod 26
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def demo():
    # Example 1: Invalid key (a=2)
    print(f"Testing a=2, b=3: {affine_encrypt('AN', 2, 3)}")
    
    # Example 2: Valid key (a=5, b=8)
    msg = "HELLO"
    encrypted = affine_encrypt(msg, 5, 8)
    print(f"Valid Encrypt (a=5, b=8): {msg} -> {encrypted}")

if __name__ == "__main__":
    demo()