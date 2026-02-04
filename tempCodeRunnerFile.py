import random

# Standard alphabet for reference
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    result = ""
    for char in text:
        if char.upper() in ALPHABET:
            # Find the index of the original letter
            index = ALPHABET.find(char.upper())
            # Replace with the letter at the same index in the key
            new_char = key[index]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.upper() in key:
            # Find the index in the scrambled key
            index = key.find(char.upper())
            # Replace with the letter at the same index in standard ALPHABET
            new_char = ALPHABET[index]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

def main():
    # Example unique key (A scrambled version of the alphabet)
    # You can change this string to any unique 26-character permutation
    cipher_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    while True:
        print("\n--- Monoalphabetic Cipher Menu ---")
        print(f"Current Key: {cipher_key}")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            msg = input("Enter plaintext: ")
            print(f"Ciphertext: {encrypt(msg, cipher_key)}")
        elif choice == '2':
            msg = input("Enter ciphertext: ")
            print(f"Plaintext: {decrypt(msg, cipher_key)}")
        elif choice == '3':
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()