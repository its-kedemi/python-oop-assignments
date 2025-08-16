 🐍 Python OOP Assignments

This repository contains solutions for Object-Oriented Programming (OOP) assignments in Python.  
The tasks explore **classes, objects, constructors, inheritance, encapsulation, and polymorphism**.

---

 📘 Assignment 1: Design Your Own Class 🏗️
- Create a class representing anything (Smartphone, Book, Superhero).
- Add attributes and methods.
- Use constructors to initialize unique values.
- Add inheritance to explore **polymorphism** or **encapsulation**.

 Example (Smartphone):
```python
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.battery += amount
        print(f"🔋 Battery charged to {self.battery}%")
🎭 Activity 2: Polymorphism Challenge
Create a program with animals or vehicles that share the same action (move()),
but behave differently depending on the class.

Example:
python
Copy
Edit
class Car:
    def move(self):
        print("🚗 Driving")

class Plane:
    def move(self):
        print("✈️ Flying")

class Boat:
    def move(self):
        print("⛵ Sailing")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
🚀 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/its-kedemi/python-oop-assignments.git
Navigate into the folder:

bash
Copy
Edit
cd "OOP Assignment"
Run any script:

bash
Copy
Edit
python3 smartphone.py
python3 polymorphism.py
✅ Requirements
Python 3.8+

No external libraries required

✨ Author
👤 Ezekiel Kedemi
🔗 GitHub Profile
