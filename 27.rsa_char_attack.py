# File Name: rsa_char_attack.py

def rsa_dictionary_attack():
    # Bob's Public Key (n is large, but that won't save him)
    n = 3233
    e = 17
    
    # Alice's intercepted ciphertext (representing 'H')
    # Let's say she encrypted the number 7 (H)
    intercepted_ciphertext = pow(7, e, n)
    print(f"Intercepted Ciphertext: {intercepted_ciphertext}")

    # --- THE ATTACK ---
    # The attacker creates a dictionary of all 26 possible encryptions
    lookup_table = {}
    for i in range(26):
        possible_ciphertext = pow(i, e, n)
        lookup_table[possible_ciphertext] = i

    # Decrypt by looking up the intercepted value
    if intercepted_ciphertext in lookup_table:
        decrypted_val = lookup_table[intercepted_ciphertext]
        char = chr(decrypted_val + 65) # Convert 0-25 back to A-Z
        print(f"Attack Success! Decrypted value is {decrypted_val} ({char})")

if __name__ == "__main__":
    rsa_dictionary_attack()