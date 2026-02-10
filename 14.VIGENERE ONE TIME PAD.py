def vigenere_otp(text, key_stream, mode='encrypt'):
    text = text.replace(" ", "").lower()
    res = []
    for i, char in enumerate(text):
        shift = key_stream[i] if mode == 'encrypt' else -key_stream[i]
        res.append(chr((ord(char) - 97 + shift) % 26 + 97))
    return "".join(res)

# Part A
p1 = "sendmoremoney"
ks1 = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
c1 = vigenere_otp(p1, ks1)
print(f"Ciphertext: {c1}")

# Part B: Find key for "cashnotneeded"
p2 = "cashnotneeded"
decoy_key = [(ord(c1[i]) - ord(p2[i])) % 26 for i in range(len(p2))]
print(f"Decoy Key: {decoy_key}")