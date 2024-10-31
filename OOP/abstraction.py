# abstraction : hiding the complexity of data and exposing only what is necessary.
# abstract base classes : module in python that provides the infrasture for defining abstract base classes
# inheritance : allows classes to inherit attribute and methods from another class
## ABC's are a way on enforcing certain methods and properties in subclasses
# baseclass (parent class)
# class A-> aB aC -> class B(inherits from A)  ->bA bb aB aC methods in class A / methods

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


    def display_message(self):
        return "This is an abstract class"

class Rectangle(shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height


        def area(self):
            return self.width * self.height


        def perimeter(self):
            return 2 * (self.width + self.height)



rect = Rectangle(10, 20)
print(rect.area())
print(rect.perimeter())
print(rect.display_message())




