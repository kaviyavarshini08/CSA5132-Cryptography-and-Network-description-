def get_matrix_inverse(matrix, mod):
    # Determinant of [[a, b], [c, d]] is (ad - bc)
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    
    # Modular multiplicative inverse of determinant
    try:
        det_inv = pow(det, -1, mod)
    except ValueError:
        return None # Matrix is not invertible

    # Adjugate matrix: [[d, -b], [-c, a]]
    adjugate = [
        [matrix[1][1] % mod, (-matrix[0][1]) % mod],
        [(-matrix[1][0]) % mod, matrix[0][0] % mod]
    ]
    
    # Inverse = (det_inv * adjugate) % mod
    return [[(cell * det_inv) % mod for cell in row] for row in adjugate]

def process_hill(text, key, mode='encrypt'):
    text = text.replace(" ", "").lower()
    if len(text) % 2 != 0: 
        text += 'x'
    
    nums = [ord(c) - 97 for c in text]
    
    if mode == 'decrypt':
        op_key = get_matrix_inverse(key, 26)
        if op_key is None:
            return "Error: Key matrix is not invertible mod 26."
    else:
        op_key = key
        
    res = []
    # Process blocks of 2
    for i in range(0, len(nums), 2):
        # Matrix multiplication: [k11 k12] * [p1]
        #                        [k21 k22]   [p2]
        p1, p2 = nums[i], nums[i+1]
        c1 = (op_key[0][0] * p1 + op_key[0][1] * p2) % 26
        c2 = (op_key[1][0] * p1 + op_key[1][1] * p2) % 26
        res.extend([c1, c2])
        
    return "".join(chr(n + 97) for n in res)

# Define key as a nested list instead of a numpy array
key = [[9, 4], 
       [5, 7]]

msg = "meetmeattheusualplaceattenratherthaneightoclock"

cipher = process_hill(msg, key, 'encrypt')
plain = process_hill(cipher, key, 'decrypt')

print(f"Ciphertext: {cipher}")
print(f"Decrypted:  {plain}")