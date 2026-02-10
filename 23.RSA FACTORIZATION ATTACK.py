import math

# 1. Known Public Info
n = 3599
e = 31
# We are told this block shares a factor with n
leaked_plaintext_block = 118 

# 2. THE ATTACK: Find the GCD
p = math.gcd(leaked_plaintext_block, n)

if p > 1:
    q = n // p
    phi = (p - 1) * (q - 1)
    
    # 3. Calculate Private Key d
    d = pow(e, -1, phi)
    
    print(f"Attack Successful!")
    print(f"Factors found: p={p}, q={q}")
    print(f"Private Key recovered: d={d}")
else:
    print("No common factor found.")