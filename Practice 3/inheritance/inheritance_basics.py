# Parent Class
class Vehicle:
    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

# Child Class 1
class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road.")

# Child Class 2
class Boat(Vehicle):
    def sail(self):
        print("Boat is sailing on water.")

# --- Testing ---
print("--- Car ---")
my_car = Car()
my_car.start_engine() # Inherited
my_car.drive()        # Own method
my_car.stop_engine()  # Inherited

print("\n--- Boat ---")
my_boat = Boat()
my_boat.start_engine()
my_boat.sail()
my_boat.stop_engine()