# allows objects to be treated as instances of the parent class.
# makes it possible to use a single interface
# for different underlying conditions
# methods overriding

class Bird:
    def sound(self):
        return "some generic bird sound"

class parrot(Bird):
    def __init__(self, name):
        self.name = name


    def sound(self):
        return "Squawks"


class Sparrow(Bird):
    def sound(self):
        return "Chirps"


par1 = parrot("parrot")
print(par1.sound())
sp1 = Sparrow()
print(sp1.sound())

