# File Name: cbc_mac_attack.py

def mock_encrypt(key, block):
    # A simple XOR-based mock encryption to demonstrate CBC logic
    # In reality, this would be AES: E_k(block)
    return (block ^ key) % 1000 

def cbc_mac_attack():
    key = 456  # Secret key unknown to adversary
    message_x = 123  # Single block message
    
    # 1. Honest MAC calculation for X
    # T = E_k(X)
    tag_t = mock_encrypt(key, message_x)
    print(f"Message X: {message_x}")
    print(f"MAC(X): {tag_t}")

    # 2. Adversary constructs a 2-block message: X || (X ^ T)
    block1 = message_x
    block2 = message_x ^ tag_t
    print(f"\nAdversary constructs 2-block message: [{block1}, {block2}]")

    # 3. Calculate MAC for the 2-block message to verify forgery
    # Step A: Process block 1
    state1 = mock_encrypt(key, block1) # This is T
    # Step B: Process block 2
    state2 = mock_encrypt(key, block2 ^ state1)
    
    print(f"MAC(X || (X ^ T)): {state2}")

    # 4. Verification
    if state2 == tag_t:
        print("\nForgery Successful! The MACs match.")

if __name__ == "__main__":
    cbc_mac_attack()