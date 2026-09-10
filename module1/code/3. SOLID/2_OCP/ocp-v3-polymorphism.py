class Employee:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return f"{self.name} is an employee"
        
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    def get_info(self):
        return f"{self.name} leads department {self.department}"
        
def print_employee(e):
    print(e.get_info())
        
e = Employee('Same')
m = Manager('Jim', 'Engineering')
print_employee(e)
print_employee(m)