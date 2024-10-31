# inheritance :allows classes to inherit attribute and methods from another class

from abc import ABC, abstractmethod

class Vehicles(ABC):
    def __init__(self, brand, make, year):
        self.brand = brand
        self.make = make
        self.year = year

    @abstractmethod
    def printReg(self, regNO):
        pass

    def display_vehicles(self):
        return f"{self.brand} {self.make} {self.year}"

class Toyota(Vehicles):
    def __init__(self, brand, make, year, speed, model):
        super().__init__(brand, make, year)  # Corrected order
        self.speed = speed
        self.model = model

    def display_toyota(self):
        return f"{self.brand} {self.make} {self.year} {self.speed} {self.model}"

    def printReg(self, regNO):
        return f"Registration Number: {regNO}"  # Corrected regNo to regNO



    @abstractmethod
    def Bestcar(self):
        pass


    def Bestcar(self, model):
        if self.model == model:
            return f"Best car in the world"
        else:

            print("Floccinihilipilication cars")


# Creating an instance of Toyota
car1 = Toyota("Toyota", "Corolla", "2/23/2024", "180km/h", "Benz")

print(car1.display_toyota())
print(car1.display_vehicles())
print(car1.printReg("KCD254"))
print(car1.Bestcar("Benz"))


