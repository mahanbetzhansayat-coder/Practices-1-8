# --- Example 1: Sort by length of string ---
fruits = ["apple", "fig", "banana", "kiwi"]
# Sort by length (shortest to longest)
by_len = sorted(fruits, key=lambda x: len(x))

# --- Example 2: Sort tuples by the second value ---
# (Name, Score)
scores = [("Alice", 50), ("Bob", 100), ("Charlie", 75)]
by_score = sorted(scores, key=lambda x: x[1])

# --- Example 3: Sort numbers by absolute value ---
nums = [-10, 5, -20, 1]
by_abs = sorted(nums, key=lambda x: abs(x))

# --- Printing ---
print(f"By length: {by_len}")
print(f"By score:  {by_score}")
print(f"By abs:    {by_abs}")