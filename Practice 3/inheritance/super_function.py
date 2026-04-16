class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Person: {self.name}, Age: {self.age}")

class Manager(Person):
    def __init__(self, name, age, department):
        # Use super() to call Parent constructor
        super().__init__(name, age)
        self.department = department

    def info(self):
        # Use super() to call Parent info method
        super().info()
        print(f"Department: {self.department}")

# --- Testing ---
m = Manager("David", 45, "IT Sales")
m.info()