# File Name: cipher_modes_padding.py

def pad(data, block_size):
    # Padding: a 1 bit followed by zeros to fill the block
    # If data is 8 bytes and block_size is 8, we add a full new block
    padding_needed = block_size - (len(data) % block_size)
    # Simplified: 0x80 represents the '1' bit followed by zeros in byte form
    padding = b'\x80' + b'\x00' * (padding_needed - 1)
    return data + padding

def unpad(data):
    # Find the last 0x80 and strip everything from there
    idx = data.rfind(b'\x80')
    return data[:idx]

def modes_demo():
    block_size = 8 # 64 bits
    message = b"HELLO!!" # Exactly 8 bytes
    
    print(f"Original: {message} (Length: {len(message)})")
    
    # Always pad, even if length is already 8
    padded = pad(message, block_size)
    print(f"Padded:   {padded.hex()} (Length: {len(padded)})")
    
    # Unpad to recover
    original = unpad(padded)
    print(f"Recovered: {original}")

if __name__ == "__main__":
    modes_demo()