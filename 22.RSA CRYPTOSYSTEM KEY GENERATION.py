def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1

# 1. Given Values
e, n = 31, 3599

# 2. Factorize n (Trial and Error / Loop)
p = next(i for i in range(2, n) if n % i == 0)
q = n // p
phi = (p - 1) * (q - 1)

# 3. Find private key d using Extended Euclidean Algorithm
# d = pow(e, -1, phi) is the easiest Python way, but here is the logic:
_, d, _ = extended_gcd(e, phi)
d = d % phi # Ensure d is positive

print(f"Primes: p={p}, q={q}")
print(f"Phi(n): {phi}")
print(f"Private Key (d): {d}")