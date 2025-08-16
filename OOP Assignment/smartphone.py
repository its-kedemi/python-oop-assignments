# smartphone.py

# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"Battery charged to {self.battery}%"

# Child Class
class SmartCameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixel):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixel = camera_megapixel

    def take_photo(self):
        return f"{self.brand} {self.model} takes a {self.camera_megapixel}MP photo 📸"

# Testing Objects
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "S23", "256GB", 80)
    phone2 = SmartCameraPhone("iPhone", "14 Pro", "512GB", 60, 48)

    print(phone1.call("0759953946"))
    print(phone1.charge(15))
    print(phone2.take_photo())
    print(phone2.charge(30))

