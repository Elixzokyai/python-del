"""
Employee payroll system
add an employee amd add a salary on the same
return total cost on payroll
"""

employee = []

"""
{
"salary" :
"name" :}
"""

def add_employee(employees, name, salary):
    return employees + [{"name" : name, "salary" : salary}]



def calculate_total_payroll(employees):
    return sum(employees["salary"] for employee in employees if employee ["salary"]> 0)

#usage
employees = add_employee(employees, "Pablo", 1000)
employees = add_employee(employees, "Grace", 1300)
total_payroll = calculate_total_payroll(employees)
print(total_payroll)
print(employees)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Bob", "40000")
print(f"{emp1.name} {emp1.salary}")

class Payroll:
    def __init__(self, salary):
