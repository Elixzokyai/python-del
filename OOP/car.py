# class keyword


class Car:
    # database table
    def __init__(self, make , model, yom, color, speed ):
        # tie the attributes to the current object
        self.make = make
        self.model = model
        self.yom = yom
        self.color = color
        self.speed = "Speed"
#     methods
    def print_name(self):
        return (f"This is the {self.make} {self.model}")
    def get_speed(self, distance):
        print(f"This is the speed of the {self.make} {self.model} {self.speed} {distance}")
## create objects
car1 = Car("Toyota","Camry","2021","Black","240")
car2 = Car("Toyota","Corolla","2010","Silver","120")
## to call method from class use the . syntax
car1.print_name()
car2.print_name()
car2.get_speed("KM/hr")