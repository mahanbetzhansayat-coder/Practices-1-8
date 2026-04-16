class Shape:
    def area(self):
        print("Area is unknown for generic shape.")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    # Overriding the area method
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area method
    def area(self):
        return 3.14 * self.radius * self.radius

# --- Testing ---
generic = Shape()
generic.area()

sq = Square(4)
print(f"Square Area: {sq.area()}")

ci = Circle(5)
print(f"Circle Area: {ci.area()}")