# --- Example 1: Simple Addition ---
def add_numbers(x, y):
    result = x + y
    return result

# --- Example 2: Calculate Area ---
def get_rectangle_area(width, height):
    area = width * height
    return area

# --- Example 3: Check if number is even ---
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# --- Example 4: Return multiple values ---
def get_min_max(numbers_list):
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    return minimum, maximum

# --- Using the return values ---

# 1. Addition
sum_val = add_numbers(10, 50)
print(f"Sum result: {sum_val}")

# 2. Area
rect_area = get_rectangle_area(5, 10)
print(f"Area result: {rect_area}")

# 3. Boolean check
number = 4
print(f"Is {number} even? {is_even(number)}")

# 4. Multiple returns
my_nums = [1, 5, 2, 9, 3]
low, high = get_min_max(my_nums)
print(f"Min: {low}, Max: {high}")