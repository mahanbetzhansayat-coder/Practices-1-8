# Regular function for comparison
def regular_double(x):
    return x * 2

# 1. Lambda for doubling a number
lambda_double = lambda x: x * 2

# 2. Lambda for adding two numbers
lambda_add = lambda x, y: x + y

# 3. Lambda for greeting
lambda_greet = lambda name: f"Hello, {name}!"

# 4. Lambda for checking if even
lambda_is_even = lambda x: x % 2 == 0

# --- Executing ---
print("Double 5 (regular):", regular_double(5))
print("Double 5 (lambda):", lambda_double(5))
print("Add 10 + 20:", lambda_add(10, 20))
print("Greeting:", lambda_greet("Student"))
print("Is 4 even?", lambda_is_even(4))