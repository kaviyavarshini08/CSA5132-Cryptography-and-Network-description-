# File Name: mono_attack.py
from collections import Counter

ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext, top_n=10):
    # 1. Count frequency of letters in ciphertext
    counts = Counter(c for c in ciphertext.upper() if c.isalpha())
    # Sort ciphertext letters by frequency
    found_freq = [item[0] for item in counts.most_common()]
    
    # 2. Map found letters to English letters
    mapping = {}
    for i in range(len(found_freq)):
        if i < len(ENGLISH_FREQ):
            mapping[found_freq[i]] = ENGLISH_FREQ[i]
            
    
    plaintext = "".join(mapping.get(c, c) for c in ciphertext.upper())
    
    return [plaintext] 

ciphertext = "Gsqqy we i xiwx qiwwyki." # Example
print(f"Top Result: {frequency_attack(ciphertext)[0]}")