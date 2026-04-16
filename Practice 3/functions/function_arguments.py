# --- Example 1: Positional Arguments ---
def describe_pet(animal_type, pet_name):
    # Order matters here
    print(f"I have a {animal_type} named {pet_name}.")

# --- Example 2: Default Arguments ---
def make_coffee(size="Medium", sugar="No"):
    # If arguments are missing, defaults are used
    print(f"Making a {size} coffee with {sugar} sugar.")

# --- Example 3: Keyword Arguments ---
def create_profile(name, age, city):
    print(f"User: {name} | Age: {age} | City: {city}")

# --- Testing the functions ---

# 1. Positional
print("--- Pets ---")
describe_pet("hamster", "Harry")
describe_pet("dog", "Rex")

# 2. Defaults
print("\n--- Coffee Order ---")
make_coffee()                    # Uses all defaults
make_coffee("Large")             # Changes size only
make_coffee("Small", "Lots of")  # Changes both

# 3. Keywords (Order doesn't matter)
print("\n--- User Profiles ---")
create_profile(age=25, city="Almaty", name="Sasha")
create_profile(name="John", city="London", age=40)