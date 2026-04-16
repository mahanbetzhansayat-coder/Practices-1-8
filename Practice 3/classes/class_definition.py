# --- Example 1: Empty Class ---
class EmptyClass:
    pass

# --- Example 2: Car Class ---
class Car:
    # A simple class attribute
    wheels = 4

# --- Creating Objects ---
car1 = Car()
car2 = Car()

# Setting attributes manually
car1.color = "Red"
car1.model = "Toyota"

car2.color = "Blue"
car2.model = "BMW"

# --- Printing ---
print(f"Car 1: {car1.color} {car1.model} with {car1.wheels} wheels")
print(f"Car 2: {car2.color} {car2.model} with {car2.wheels} wheels")