def encrypt_rail_fence(text, rails):
    # Create a matrix to visualize the rails
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    
    # Fill the rails in a zig-zag manner
    rail = 0
    direction = 1 # 1 for down, -1 for up
    
    for i in range(len(text)):
        fence[rail][i] = text[i]
        rail += direction
        
        # Change direction at the top or bottom rail
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    # Read the fence row by row
    result = []
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                result.append(fence[i][j])
    return "".join(result)

def decrypt_rail_fence(cipher, rails):
    # Create a template matrix
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    
    # Mark the zig-zag spots with '*'
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    # Fill the marked spots with the ciphertext characters
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1
                
    # Read the fence in zig-zag order to get plaintext
    result = []
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    return "".join(result)

def main():
    while True:
        print("\n--- Rail Fence Cipher Menu ---")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '3':
            break
            
        if choice in ['1', '2']:
            msg = input("Enter your message: ")
            try:
                num_rails = int(input("Enter number of rails: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
                
            if choice == '1':
                print(f"Encrypted: {encrypt_rail_fence(msg, num_rails)}")
            else:
                print(f"Decrypted: {decrypt_rail_fence(msg, num_rails)}")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()