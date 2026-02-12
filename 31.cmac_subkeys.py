# File Name: cmac_subkeys.py

def generate_subkeys(block_size):
    # Setup constants based on block size
    if block_size == 128:
        rb = 0x87
        mask = (1 << 128) - 1
        msb_mask = 1 << 127
    else: # 64-bit
        rb = 0x1B
        mask = (1 << 64) - 1
        msb_mask = 1 << 63

    # Step 1: L = E(K, 0^b). Here we simulate L with a dummy value
    L = 0b101100  # Assume this is the result of encrypting zeros
    print(f"L (Result of E(K, 0)): {hex(L)}")

    # Step 2: Generate K1
    if L & msb_mask:
        k1 = ((L << 1) & mask) ^ rb
    else:
        k1 = (L << 1) & mask
    
    # Step 3: Generate K2
    if k1 & msb_mask:
        k2 = ((k1 << 1) & mask) ^ rb
    else:
        k2 = (k1 << 1) & mask

    print(f"Subkey K1: {hex(k1)}")
    print(f"Subkey K2: {hex(k2)}")

if __name__ == "__main__":
    print("--- 64-bit CMAC Subkeys ---")
    generate_subkeys(64)