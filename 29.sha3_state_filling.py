# File Name: sha3_state_filling.py

def simulate_sha3_filling():
    # SHA-3-1600 parameters
    total_lanes = 25
    bitrate_lanes = 16  # 1024 bits / 64
    capacity_lanes = 9   # 25 - 16
    
    # Initial state: all zeros (List of 25 lanes)
    state = [0] * total_lanes
    
    print(f"Initial State: {state}")
    
    # P0 (First message block) - assume each lane has at least one nonzero bit
    # We will represent a nonzero lane with the value 1
    p0 = [1] * bitrate_lanes
    
    # XOR P0 into the bitrate portion of the state
    for i in range(bitrate_lanes):
        state[i] = state[i] ^ p0[i]
        
    print("\n--- After XORing P0 (Before Permutation) ---")
    print(f"Bitrate Lanes (0-15): {state[:16]}")
    print(f"Capacity Lanes (16-24): {state[16:]}")
    
    zero_capacity_count = state[16:].count(0)
    print(f"\nCapacity lanes still zero: {zero_capacity_count}")
    print("Result: Capacity lanes remain zero until the first Keccak-f permutation.")

if __name__ == "__main__":
    simulate_sha3_filling()