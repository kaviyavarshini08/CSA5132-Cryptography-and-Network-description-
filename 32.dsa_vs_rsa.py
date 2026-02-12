# File Name: dsa_vs_rsa.py
import random

def rsa_sign(m, d, n):
    # Deterministic: Same input, same output
    return pow(m, d, n)

def dsa_sign_logic(m, x, q, g):
    # Non-deterministic: Uses random 'k'
    k = random.randint(1, q-1)
    r = pow(g, k, q) # Simplified logic
    s = (k + m * x) % q # Mock DSA formula
    return (r, s, k)

def compare_signatures():
    # Mock parameters
    msg = 100
    priv_key = 5
    modulus = 997
    
    print(f"Message: {msg}")
    
    # RSA Example
    sig1_rsa = rsa_sign(msg, priv_key, modulus)
    sig2_rsa = rsa_sign(msg, priv_key, modulus)
    print(f"\nRSA Sig 1: {sig1_rsa}")
    print(f"RSA Sig 2: {sig2_rsa}")
    print("RSA Result: Identical")

    # DSA Example
    r1, s1, k1 = dsa_sign_logic(msg, priv_key, modulus, 2)
    r2, s2, k2 = dsa_sign_logic(msg, priv_key, modulus, 2)
    print(f"\nDSA Sig 1 (r, s): ({r1}, {s1}) | k used: {k1}")
    print(f"DSA Sig 2 (r, s): ({r2}, {s2}) | k used: {k2}")
    print("DSA Result: Different (due to random k)")

if __name__ == "__main__":
    compare_signatures()