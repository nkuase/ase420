class Employee:
    def __init__(self, name):
        self.name = name
        
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        
def print_employee(e):
    if type(e) is Employee:
        print(f"{e.name} is an employee")
    elif type(e) is Manager:
        print(f"{e.name} leads department {e.department}")
        
e = Employee('Same')
m = Manager('Jim', 'Engineering')
print_employee(e)
print_employee(m)