# Data list
numbers = [1, 2, 3, 4, 5]

# --- Example 1: Square numbers ---
squared = list(map(lambda x: x ** 2, numbers))

# --- Example 2: Cube numbers ---
cubed = list(map(lambda x: x ** 3, numbers))

# --- Example 3: Add 10 to each number ---
added = list(map(lambda x: x + 10, numbers))

# --- Example 4: Uppercase strings ---
words = ["apple", "banana", "cherry"]
uppercased = list(map(lambda w: w.upper(), words))

# --- Printing ---
print(f"Original: {numbers}")
print(f"Squared:  {squared}")
print(f"Cubed:    {cubed}")
print(f"Plus 10:  {added}")
print(f"Words:    {uppercased}")