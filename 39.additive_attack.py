# File Name: additive_attack.py

def additive_attack(ciphertext, top_n=10):
    # Frequency of letters in English
    eng_freq = {'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0}
    results = []

    for shift in range(26):
        decrypted = ""
        for char in ciphertext.upper():
            if char.isalpha():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += char
        
        # Simple scoring: count how many high-frequency English letters appear
        score = sum(decrypted.count(letter) for letter in "ETAOIN")
        results.append((score, decrypted))

    # Sort by score descending and return top N
    results.sort(key=lambda x: x[0], reverse=True)
    return [res[1] for res in results[:top_n]]

if __name__ == "__main__":
    ct = "KHOOR ZRUOG" # "HELLO WORLD" shifted by 3
    top_10 = additive_attack(ct, 10)
    for i, p in enumerate(top_10):
        print(f"{i+1}: {p}")