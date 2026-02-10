# S-DES Tables and Logic
P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6); P8 = (6, 3, 7, 4, 8, 5, 10, 9)
IP = (2, 6, 3, 1, 4, 8, 5, 7); IPI = (4, 1, 3, 5, 7, 2, 8, 6)
EP = (4, 1, 2, 3, 2, 3, 4, 1); P4 = (2, 4, 3, 1)
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]; S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def perm(bits, table): return "".join(bits[i-1] for i in table)

def fk(bits, k):
    L, R = bits[:4], bits[4:]
    ex = perm(R, EP)
    xor = bin(int(ex, 2) ^ int(k, 2))[2:].zfill(8)
    s = lambda b, m: bin(m[int(b[0]+b[3],2)][int(b[1]+b[2],2)])[2:].zfill(2)
    res = perm(s(xor[:4], S0) + s(xor[4:], S1), P4)
    return bin(int(L, 2) ^ int(res, 2))[2:].zfill(4) + R

# Key Generation
key = perm("0111111101", P10)
L, R = key[:5], key[5:]
k1 = perm((L[1:]+L[:1]) + (R[1:]+R[:1]), P8)
k2 = perm((L[3:]+L[:3]) + (R[3:]+R[:3]), P8)

def sdes_encrypt(b):
    b = perm(b, IP)
    b = fk(b, k1)
    b = fk(b[4:] + b[:4], k2)
    return perm(b, IPI)

def ctr_process(data):
    result = ""
    for i in range(0, len(data), 8):
        # 1. Encrypt the current counter index (0, 1, 2...) formatted as 8 bits
        counter_bits = bin(i // 8)[2:].zfill(8)
        keystream_block = sdes_encrypt(counter_bits)
        
        # 2. XOR the keystream with the data block
        data_block = data[i:i+8]
        xor_res = bin(int(data_block, 2) ^ int(keystream_block, 2))[2:].zfill(8)
        result += xor_res
    return result

# --- Execution ---
plaintext = "000000010000001000000100"
ciphertext = ctr_process(plaintext)
decrypted = ctr_process(ciphertext)

print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted:  {decrypted}")