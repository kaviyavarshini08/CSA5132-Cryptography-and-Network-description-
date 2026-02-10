def matrix_mod_inv(matrix, mod):
    # Corrected Determinant: (ad - bc)
    # matrix[0][0]=a, matrix[0][1]=b, matrix[1][0]=c, matrix[1][1]=d
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    
    # Find modular inverse of determinant using pow(n, -1, mod)
    try:
        det_inv = pow(det, -1, mod)
    except ValueError:
        return "Determinant has no inverse; these pairs cannot recover the key."

    # Adjugate for 2x2: [[d, -b], [-c, a]]
    adj = [[matrix[1][1], -matrix[0][1]], 
           [-matrix[1][0], matrix[0][0]]]
    
    return [[(cell * det_inv) % mod for cell in row] for row in adj]

def known_plaintext_attack(p_text, c_text):
    # Map letters to numbers
    p_nums = [ord(c) - 97 for c in p_text]
    c_nums = [ord(c) - 97 for c in c_text]
    
    # Construct 2x2 matrices where columns are letter pairs
    P = [[p_nums[0], p_nums[2]], 
         [p_nums[1], p_nums[3]]]
    
    C = [[c_nums[0], c_nums[2]], 
         [c_nums[1], c_nums[3]]]
    
    P_inv = matrix_mod_inv(P, 26)
    
    if isinstance(P_inv, str): return P_inv

    # Matrix Multiply: K = C * P_inv
    K = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            K[i][j] = sum(C[i][k] * P_inv[k][j] for k in range(2)) % 26
    return K

# Testing with an example pair
# If 'me' (12, 4) -> 'ze' (25, 4) and 'at' (0, 19) -> 'lh' (11, 7)
res = known_plaintext_attack("meat", "zelh")
print("Recovered Key Matrix:")
for row in res:
    print(row)