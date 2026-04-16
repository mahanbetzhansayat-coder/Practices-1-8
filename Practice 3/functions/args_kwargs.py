# --- Example 1: *args (Arbitrary Arguments) ---
# Useful when we don't know how many items will be passed
def shop_list(*items):
    print("Shopping List:")
    for item in items:
        print(f"- {item}")

# --- Example 2: Summing with *args ---
def calculate_total(*prices):
    total = sum(prices)
    print(f"Total price: ${total}")

# --- Example 3: **kwargs (Arbitrary Keyword Arguments) ---
# Useful for dictionaries or profiles
def print_student_info(**details):
    print("\nStudent Details:")
    # Loop through the dictionary keys and values
    for key, value in details.items():
        print(f"{key}: {value}")

# --- Testing ---

# Using args
shop_list("Apples", "Bananas", "Milk", "Bread")
calculate_total(10, 20, 5, 5)

# Using kwargs
print_student_info(name="Alibek", course="Python", year=2)
print_student_info(name="Dina", grade="A", city="Astana")