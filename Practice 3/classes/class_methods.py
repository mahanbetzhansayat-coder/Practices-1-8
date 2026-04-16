class Calculator:
    def __init__(self):
        self.history = []

    # Method to add
    def add(self, a, b):
        res = a + b
        self.history.append(f"{a} + {b} = {res}")
        return res

    # Method to subtract
    def subtract(self, a, b):
        res = a - b
        self.history.append(f"{a} - {b} = {res}")
        return res

    # Method to show history
    def show_history(self):
        print("Calculation History:")
        for record in self.history:
            print(record)

# --- Testing Methods ---
calc = Calculator()

print("Result 1:", calc.add(10, 5))
print("Result 2:", calc.subtract(20, 8))
print("Result 3:", calc.add(100, 200))

print()
calc.show_history()