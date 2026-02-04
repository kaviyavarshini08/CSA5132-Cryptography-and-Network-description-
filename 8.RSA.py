import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(pk, plaintext):
    key, n = pk
    # (m ^ e) % n
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    # (c ^ d) % n
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# Basic Key Generation for Lab
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
# Calculate d (modular inverse)
d = pow(e, -1, phi)

public = (e, n)
private = (d, n)

msg = "HELLO"
enc = encrypt(public, msg)
print(f"Encrypted: {enc}")
print(f"Decrypted: {decrypt(private, enc)}")