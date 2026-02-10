from collections import Counter

def frequency_attack(cipher, top_n=10):
    freq_order = "etaoinshrdlcumwfgypbvkjxqz"
    results = []
    
    for shift in range(26):
        plain = "".join(chr((ord(c) - 97 - shift) % 26 + 97) for c in cipher)
        # Score based on common letters
        counts = Counter(plain)
        score = sum(counts.get(char, 0) for char in freq_order[:6])
        results.append((score, plain))
    
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:top_n]]

cipher_input = "vqrpsvqrps" # Example
print("Top 10 Plaintexts:")
for i, p in enumerate(frequency_attack(cipher_input), 1):
    print(f"{i}. {p}")