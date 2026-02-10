# S-DES Constants
P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
IP = (2, 6, 3, 1, 4, 8, 5, 7)
IP_INV = (4, 1, 3, 5, 7, 2, 8, 6)
EP = (4, 1, 2, 3, 2, 3, 4, 1)
P4 = (2, 4, 3, 1)
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(bits, table):
    return "".join(bits[i - 1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_keys(key):
    key = permute(key, P10)
    left, right = key[:5], key[5:]
    # Key 1
    left, right = left_shift(left, 1), left_shift(right, 1)
    k1 = permute(left + right, P8)
    # Key 2
    left, right = left_shift(left, 2), left_shift(right, 2)
    k2 = permute(left + right, P8)
    return k1, k2

def f_k(bits, key):
    L, R = bits[:4], bits[4:]
    expanded = permute(R, EP)
    xor_val = bin(int(expanded, 2) ^ int(key, 2))[2:].zfill(8)
    
    def s_box(b, s):
        row = int(b[0] + b[3], 2)
        col = int(b[1] + b[2], 2)
        return bin(s[row][col])[2:].zfill(2)

    val = s_box(xor_val[:4], S0) + s_box(xor_val[4:], S1)
    val = permute(val, P4)
    return bin(int(L, 2) ^ int(val, 2))[2:].zfill(4) + R

def sdes_encrypt(block, k1, k2):
    block = permute(block, IP)
    block = f_k(block, k1)
    block = block[4:] + block[:4] # Switch
    block = f_k(block, k2)
    return permute(block, IP_INV)

def sdes_decrypt(block, k1, k2):
    block = permute(block, IP)
    block = f_k(block, k2) # K2 first for decryption
    block = block[4:] + block[:4]
    block = f_k(block, k1)
    return permute(block, IP_INV)

# --- CBC MODE LOGIC ---
def cbc_encrypt(plaintext, key, iv):
    k1, k2 = generate_keys(key)
    blocks = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    ciphertext = ""
    prev_block = iv
    
    for p in blocks:
        # XOR with previous ciphertext (or IV)
        xor_res = bin(int(p, 2) ^ int(prev_block, 2))[2:].zfill(8)
        encrypted = sdes_encrypt(xor_res, k1, k2)
        ciphertext += encrypted
        prev_block = encrypted
    return ciphertext

# --- TEST DATA ---
iv = "10101010"
key = "0111111101"
plaintext = "0000000100100011"

cipher_out = cbc_encrypt(plaintext, key, iv)

print(f"Key: {key}")
print(f"IV:  {iv}")
print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {cipher_out}")