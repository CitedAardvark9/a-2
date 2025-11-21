# operators_example.py
# Interactable list of common Python operators with explanations.

# Try changing the values below to experiment.
a = 10
b = 3

print("\n=== ARITHMETIC OPERATORS ===")
print(f"{a} + {b} = {a + b}")      # Addition
print(f"{a} - {b} = {a - b}")      # Subtraction
print(f"{a} * {b} = {a * b}")      # Multiplication
print(f"{a} / {b} = {a / b}")      # Division (always float)
print(f"{a} // {b} = {a // b}")    # Floor division (drops decimals)
print(f"{a} % {b} = {a % b}")      # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")    # Exponent (a^b)

print("\n=== COMPARISON OPERATORS ===")
print(f"{a} == {b} → {a == b}")    # Equal to
print(f"{a} != {b} → {a != b}")    # Not equal
print(f"{a} > {b}  → {a > b}")     # Greater than
print(f"{a} < {b}  → {a < b}")     # Less than
print(f"{a} >= {b} → {a >= b}")    # Greater or equal
print(f"{a} <= {b} → {a <= b}")    # Less or equal

print("\n=== LOGICAL OPERATORS ===")
x = True
y = False
print(f"{x} and {y} → {x and y}")  # True only if both are True
print(f"{x} or {y} → {x or y}")    # True if at least one is True
print(f"not {x} → {not x}")        # Negates a boolean

print("\n=== ASSIGNMENT OPERATORS ===")
c = 5
print(f"Starting c = {c}")
c += 2     # c = c + 2
print(f"c += 2 → {c}")
c *= 3     # c = c * 3
print(f"c *= 3 → {c}")
c -= 4     # c = c - 4
print(f"c -= 4 → {c}")

print("\n=== MEMBERSHIP OPERATORS ===")
nums = [1, 2, 3, 4]
print(f"List: {nums}")
print(f'2 in nums → {2 in nums}')       # Checks if a value exists in a list
print(f'7 not in nums → {7 not in nums}')

print("\n=== IDENTITY OPERATORS ===")
# 'is' checks if two variables point to the SAME object in memory
m = [1, 2]
n = m     # n references the same object as m
p = [1, 2]  # p is a separate object with same content
print(f"m is n → {m is n} (same object)")
print(f"m is p → {m is p} (same content, different object)")
print(f"m == p → {m == p} (same value)")

print("\n--- END OF OPERATOR DEMO ---\n")
