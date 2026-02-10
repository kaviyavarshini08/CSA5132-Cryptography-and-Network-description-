def create_matrix(key):
    key = key.upper().replace("J", "I").replace(" ", "")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    seen = set()
    for char in key + alphabet:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for r, row in enumerate(matrix):
        if char in row: return r, row.index(char)

def decrypt_playfair(ciphertext, key):
    matrix = create_matrix(key)
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(matrix, ciphertext[i])
        r2, c2 = find_pos(matrix, ciphertext[i+1])
        
        if r1 == r2: # Same row
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2: # Same column
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else: # Rectangle
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

cipher = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"
key = "ROYAL NEW ZEALAND NAVY"
print(f"Decrypted Message: {decrypt_playfair(cipher, key)}")