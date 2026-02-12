# File Name: monoalphabetic_frequency_attack.py
from collections import Counter

# Standard English letters ordered by frequency (highest to lowest)
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def get_score(text):
    """Scores text based on common English letter presence."""
    common_letters = set("ETAOIN")
    score = sum(1 for char in text.upper() if char in common_letters)
    return score

def frequency_attack(ciphertext, top_n=10):
    # 1. Clean and count ciphertext frequencies
    letters_only = [c for c in ciphertext.upper() if c.isalpha()]
    counts = Counter(letters_only).most_common()
    cipher_freq_order = "".join([item[0] for item in counts])

    # 2. Since we need 'top_n' likelihoods, we generate variations.
    # A basic attack maps cipher_freq_order directly to ENGLISH_FREQ_ORDER.
    # To get multiple possibilities, we can slightly shift the frequency map.
    
    results = []
    
    # Try different starting offsets in the English frequency table
    for shift in range(min(len(cipher_freq_order), top_n)):
        # Create a mapping table
        mapping = {}
        # Adjust the English frequency alignment slightly for variation
        adjusted_english = ENGLISH_FREQ_ORDER[shift:] + ENGLISH_FREQ_ORDER[:shift]
        
        for i, char in enumerate(cipher_freq_order):
            if i < len(adjusted_english):
                mapping[char] = adjusted_english[i]
        
        # Translate the ciphertext
        decrypted = ""
        for char in ciphertext.upper():
            if char.isalpha():
                decrypted += mapping.get(char, char)
            else:
                decrypted += char
        
        results.append(decrypted)

    # Sort results by likelihood (simple scoring)
    results.sort(key=get_score, reverse=True)
    return results[:top_n]

if __name__ == "__main__":
    # Example ciphertext (A simple substitution)
    # Original: "HELLO WORLD THIS IS A TEST"
    ct = "IFMMP XPSME UIJT JT B UFTU" 
    
    try:
        num = int(input("How many possible plaintexts would you like to see? (e.g., 10): "))
    except ValueError:
        num = 10

    candidates = frequency_attack(ct, num)
    
    print(f"\n--- Top {num} Possible Plaintexts ---")
    for i, guess in enumerate(candidates, 1):
        print(f"{i}. {guess}")