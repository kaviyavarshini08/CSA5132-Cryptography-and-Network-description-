# PC-1 and PC-2 Permutation tables and Shift schedule
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_decryption_keys(main_key_bits):
    # 1. Initial Permutation (PC-1) would happen here
    # Splitting 56-bit key into two 28-bit halves (C and D)
    C, D = main_key_bits[:28], main_key_bits[28:]
    subkeys = []

    # 2. Generate all 16 subkeys
    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        # In reality, PC-2 permutation is applied here to get 48-bit K
        subkeys.append(C + D) 

    # 3. For DECRYPTION, reverse the subkey list
    decryption_keys = subkeys[::-1]
    return decryption_keys

# Example: 56-bit dummy key
dummy_key = "1" * 56
keys = generate_decryption_keys(dummy_key)
print(f"Total Decryption Subkeys Generated: {len(keys)}")
print(f"First Subkey for Decryption (K16): {keys[0][:10]}...")