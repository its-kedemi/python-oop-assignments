# vehicles.py

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Testing Polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())

