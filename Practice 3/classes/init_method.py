class Student:
    # Constructor method
    def __init__(self, name, student_id, major):
        print(f"Creating student: {name}...")
        self.name = name
        self.id = student_id
        self.major = major

    # A simple method to show info
    def display(self):
        print(f"ID: {self.id} | Name: {self.name} | Major: {self.major}")

# --- Creating 3 Students ---
s1 = Student("Alice", "001", "Computer Science")
s2 = Student("Bob",   "002", "Mathematics")
s3 = Student("Eve",   "003", "Physics")

print("\n--- Student List ---")
s1.display()
s2.display()
s3.display()