# File Name: hill_attack.py
import numpy as np

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)
    return (det_inv * adjugate) % modulus

def hill_known_plaintext_attack():
    # Known Plaintext: 'HELP' -> [7, 4], [11, 15]
    P = np.array([[7, 4], [11, 15]]) 
    # Known Ciphertext
    C = np.array([[3, 2], [5, 12]]) # Dummy values
    
    try:
        P_inv = matrix_mod_inv(P, 26)
        K = (P_inv @ C) % 26
        print("Recovered Key Matrix:")
        print(K)
    except ValueError:
        print("Matrix not invertible. Need more/different plaintext pairs.")

if __name__ == "__main__":
    hill_known_plaintext_attack()