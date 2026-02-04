# 1. Setup the alphabet mapping (A=0, B=1, ... Z=25)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 2. Get input from the user
text = input("Enter the message (UPPERCASE): ").upper()
k = int(input("Enter the key (K): "))

# 3. Encryption Process: C = (P + K) mod 26
encrypted_result = ""
for letter in text:
    if letter in alphabet:
        p = alphabet.index(letter)
        c = (p + k) % 26
        encrypted_result += alphabet[c]
    else:
        encrypted_result += letter

# 4. Decryption Process: P = (C - K) mod 26
# (We use the encrypted_result as the input to prove it works)
decrypted_result = ""
for letter in encrypted_result:
    if letter in alphabet:
        c = alphabet.index(letter)
        p = (c - k) % 26
        decrypted_result += alphabet[p]
    else:
        decrypted_result += letter

# 5. Output both results
print("-" * 30)
print(f"Original Text:  {text}")
print(f"Key (K):        {k}")

print(f"ENCRYPTED (C):  {encrypted_result}") # This uses (P + K) mod 26
print(f"DECRYPTED (P):  {decrypted_result}")  # This uses (C - K) mod 26
