# Encapsulation : refers to bundling data and methods that work on the data in a single unit called

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        self.dateofreg = "11-2-2024"

    def display_employee(self):
            return f"Employee Name: {self.name}, Salary: {self.salary} : {self.dateofreg}"


    def update_salary(self, amount):
            if amount > 0:
                self.salary += amount
            else:
                print("Salary cannot be negative")


                #create an object

empl = Employee("Pablo", "150000")
print(empl.display_employee())
print(empl.name)
print(empl.update_salary(50000))
print(empl.display_employee())
