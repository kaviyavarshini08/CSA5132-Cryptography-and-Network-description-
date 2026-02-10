import math

# Total possible keys
total_keys = math.factorial(25)
power_of_2 = math.log2(total_keys)

# Unique keys (accounting for grid shifts)
unique_keys = total_keys // 25

print(f"Total keys: ~2^{power_of_2:.2f}")
print(f"Effectively unique keys: {unique_keys}")