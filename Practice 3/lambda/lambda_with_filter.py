# Data list
values = [10, -5, 3, -1, 0, 8, 12]

# --- Example 1: Positive numbers ---
positives = list(filter(lambda x: x > 0, values))

# --- Example 2: Negative numbers ---
negatives = list(filter(lambda x: x < 0, values))

# --- Example 3: Even numbers ---
evens = list(filter(lambda x: x % 2 == 0, values))

# --- Example 4: Filter short words ---
words = ["hi", "hello", "yo", "greetings", "a"]
short_words = list(filter(lambda w: len(w) <= 2, words))

# --- Printing ---
print(f"All values: {values}")
print(f"Positives:  {positives}")
print(f"Negatives:  {negatives}")
print(f"Evens:      {evens}")
print(f"Short words:{short_words}")