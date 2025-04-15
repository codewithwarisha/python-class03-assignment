# ----------------------
#  Lesson 07: Set and Frozenset Usage
# ----------------------

# Set: Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("🔢 Unique Numbers:", unique_numbers)

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("\n➕ Union:", set_a | set_b)
print("➖ Difference:", set_a - set_b)
print("✖️ Intersection:", set_a & set_b)

# Frozenset: Immutable Set
frozen = frozenset(["apple", "banana", "cherry"])
print("\n🍎 Frozenset Example:", frozen)
