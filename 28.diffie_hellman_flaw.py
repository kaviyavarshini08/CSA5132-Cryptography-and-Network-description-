# File Name: diffie_hellman_flaw.py

def diffie_hellman():
    # Publicly shared values (a is the base, q is the prime modulus)
    a = 5 
    q = 23

    # 1. Alice's Side
    alice_secret = 6
    alice_public = pow(a, alice_secret, q)
    print(f"Alice sends: {alice_public}")

    # 2. Bob's Side
    bob_secret = 15
    bob_public = pow(a, bob_secret, q)
    print(f"Bob sends: {bob_public}")

    # --- Key Agreement ---
    # Alice computes key using Bob's public value
    alice_key = pow(bob_public, alice_secret, q)
    
    # Bob computes key using Alice's public value
    bob_key = pow(alice_public, bob_secret, q)

    print(f"Alice's Key: {alice_key}")
    print(f"Bob's Key: {bob_key}")
    
    # Verification
    if alice_key == bob_key:
        print("Success! Shared secret key established.")

if __name__ == "__main__":
    diffie_hellman()