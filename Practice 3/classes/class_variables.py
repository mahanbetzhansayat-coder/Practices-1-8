class Laptop:
    # Class variable (same for all laptops)
    brand = "Generic Brand"

    def __init__(self, model, ram):
        # Instance variables (different for each laptop)
        self.model = model
        self.ram = ram

# Creating instances
l1 = Laptop("ProBook", "8GB")
l2 = Laptop("AirBook", "16GB")

print(f"Laptop 1: {l1.brand} {l1.model}")
print(f"Laptop 2: {l2.brand} {l2.model}")

print("\n--- Changing Class Variable ---")
# Changing the brand for ALL laptops
Laptop.brand = "SuperTech"

print(f"Laptop 1: {l1.brand} {l1.model}")
print(f"Laptop 2: {l2.brand} {l2.model}")