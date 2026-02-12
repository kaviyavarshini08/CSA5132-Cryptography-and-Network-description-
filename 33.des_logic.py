
# File Name: des_logic.py

def simple_feistel(block, key):
    # Simplified Feistel: XOR half the block with the key
    left = block >> 32
    right = block & 0xFFFFFFFF
    
    # f-function: (right XOR key)
    new_right = left ^ (right ^ key)
    new_left = right
    
    return (new_left << 32) | new_right

def des_demo():
    # 64-bit Plaintext and 56-bit Key (represented as integers)
    plaintext = 0x0123456789ABCDEF
    key = 0x133457799BBCDFF1 # 56 bits (with parity)
    
    print(f"Input Plaintext: {hex(plaintext)}")
    
    # One Round of DES-like structure
    ciphertext = simple_feistel(plaintext, key & 0xFFFFFFFF)
    print(f"Ciphertext after 1 round: {hex(ciphertext)}")
    
    # Decryption (Same logic, reversed rounds)
    decrypted = simple_feistel(ciphertext, key & 0xFFFFFFFF)
    print(f"Decrypted Result: {hex(decrypted)}")

if __name__ == "__main__":
    des_demo()
