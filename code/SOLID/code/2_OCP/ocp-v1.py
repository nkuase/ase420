class Employee:
    def __init__(self, name):
        self.name = name
        
def print_employee(e):
    print(f"{e.name} is an employee")
    
e = Employee("Sam")
print_employee(e)