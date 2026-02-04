def text_to_numbers(text):
    # Converts text to a string of numbers separated by spaces
    result = []
    for char in text:
        if char.isalpha():
            # A=1, B=2... Z=26
            number = ord(char.upper()) - ord('A') + 1
            result.append(str(number))
        else:
            # Keeps spaces or punctuation as they are
            result.append(char)
    return " ".join(result)

def numbers_to_text(numeric_string):
    # Converts space-separated numbers back to text
    result = ""
    parts = numeric_string.split()
    for part in parts:
        if part.isdigit():
            # Converts number back to character
            char = chr(int(part) + ord('A') - 1)
            result += char
        else:
            # Handles non-numeric parts
            result += part
    return result

def main():
    while True:
        print("\n--- Numeric Substitution Menu ---")
        print("1. Encryption (Text to Numbers)")
        print("2. Decryption (Numbers to Text)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            msg = input("Enter text to encrypt: ")
            print(f"Numeric Output: {text_to_numbers(msg)}")
        elif choice == '2':
            msg = input("Enter numbers to decrypt (separated by spaces): ")
            print(f"Text Output: {numbers_to_text(msg)}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()