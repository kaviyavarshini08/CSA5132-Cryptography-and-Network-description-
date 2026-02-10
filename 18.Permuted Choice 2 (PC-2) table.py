# Permuted Choice 2 (PC-2) table
# Bits 1-24 come from the first 28-bit half (C)
# Bits 25-48 come from the second 28-bit half (D)
PC2 = (
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
)

# Number of left shifts for each of the 16 rounds
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_des_subkeys(initial_56bit_key):
    # Split the 56-bit key into two disjoint 28-bit subsets
    C = initial_56bit_key[:28]
    D = initial_56bit_key[28:]
    
    subkeys = []
    
    for round_num, shift in enumerate(SHIFT_SCHEDULE):
        # Shift each half independently
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        
        # Combine halves and apply PC-2
        combined = C + D
        subkey = "".join(combined[i-1] for i in PC2)
        
        subkeys.append(subkey)
        
        # Display the split nature of the subkey
        first_half_subkey = subkey[:24]
        second_half_subkey = subkey[24:]
        print(f"Round {round_num+1:2}: K_left(24b): {first_half_subkey} | K_right(24b): {second_half_subkey}")

# Example: A 56-bit key (represented as a string of '0's and '1's)
example_key = "1" * 28 + "0" * 28  # First 28 bits are '1', second 28 bits are '0'
generate_des_subkeys(example_key)