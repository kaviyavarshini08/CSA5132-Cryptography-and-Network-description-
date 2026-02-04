import math

# 1. Inputs
msg = input("Enter message: ")
key = input("Enter keyword: ").upper()

# --- ENCRYPTION LOGIC ---
cols = len(key)
rows = math.ceil(len(msg) / cols)
# Add padding '_' like your code did
msg_padded = msg + ("_" * ((rows * cols) - len(msg)))

# Create Matrix (Row-wise)
matrix = [msg_padded[i:i+cols] for i in range(0, len(msg_padded), cols)]

# Determine alphabetical order of key (HACK -> ACHK)
key_order = sorted(range(len(key)), key=lambda k: key[k])

# Read Matrix Column-wise based on key order
cipher = ""
for col_idx in key_order:
    for row in matrix:
        cipher += row[col_idx]

# --- DECRYPTION LOGIC ---
# Create empty matrix to fill
dec_matrix = [[None] * cols for _ in range(rows)]
cipher_list = list(cipher)
curr_char = 0

# Fill Matrix Column-wise according to alphabetical key
for col_idx in key_order:
    for row_idx in range(rows):
        dec_matrix[row_idx][col_idx] = cipher_list[curr_char]
        curr_char += 1

# Read Matrix Row-wise to get original message
decrypted = "".join(["".join(row) for row in dec_matrix]).replace("_", "")

print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypted}")