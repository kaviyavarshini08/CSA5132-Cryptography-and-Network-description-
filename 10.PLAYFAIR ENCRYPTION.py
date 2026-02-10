def find_pos(matrix, char):
    # Standard Playfair treats I and J as the same
    char = 'I' if char == 'J' else char
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def encrypt_playfair(plaintext, matrix_rows):
    # Convert input list of strings into a 2D list of characters
    matrix = [list(row.replace("I/J", "I")) for row in matrix_rows]
    
    # Prepare plaintext: Upper case, replace J with I, remove non-alphabetic
    plaintext = "".join(filter(str.isalpha, plaintext.upper().replace("J", "I")))
    
    prepared = ""
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i+1]
            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "X"
            i += 1

    ciphertext = ""
    for i in range(0, len(prepared), 2):
        r1, c1 = find_pos(matrix, prepared[i])
        r2, c2 = find_pos(matrix, prepared[i+1])
        
        if r1 == r2: # Rule: Same Row
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2: # Rule: Same Column
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else: # Rule: Rectangle (Swap Columns)
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
            
    return ciphertext

# Custom matrix from Question 10
custom_matrix = ["MFHIK", "UNOPQ", "ZVWXY", "ELARG", "DSTBC"]
msg = "Must see you over Cadogan West. Coming at once."

result = encrypt_playfair(msg, custom_matrix)
print(f"Encrypted Message: {result}")