# --- Example 1: Simple Greeting ---
def say_hello():
    # This function just prints a static message
    print("Hello! Welcome to the system.")

# --- Example 2: Greeting with a Name ---
def greet_user(username):
    # This function accepts one argument
    print(f"Good morning, {username}!")

# --- Example 3: Simple Instruction ---
def show_rules():
    print("Rule 1: Be polite.")
    print("Rule 2: Write clean code.")
    print("Rule 3: Have fun.")

# --- Example 4: Goodbye Message ---
def say_goodbye():
    print("Goodbye! See you later.")

# --- Calling all functions below ---
print("--- Start Program ---")
say_hello()
print() # Empty line for readability

greet_user("Alice")
greet_user("Bob")
print()

show_rules()
print()

say_goodbye()
print("--- End Program ---")