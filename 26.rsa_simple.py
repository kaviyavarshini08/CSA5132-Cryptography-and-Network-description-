import math

# RSA logic with small numbers for clarity
def rsa_demo():
    # 1. Choose two small primes
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)

    # 2. Public Key (e)
    e = 17
    
    # 3. Private Key (d) - modular inverse of e
    d = pow(e, -1, phi)

    print(f"Keys Generated: Public(e={e}, n={n}), Private(d={d}, n={n})")

    # 4. Encryption: ciphertext = (msg^e) % n
    msg = 42
    encrypted = pow(msg, e, n)
    print(f"Message {msg} encrypted to: {encrypted}")

    # 5. Decryption: message = (ctext^d) % n
    decrypted = pow(encrypted, d, n)
    print(f"Ciphertext decrypted back to: {decrypted}")

if __name__ == "__main__":
    rsa_demo()