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

class Programmer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self. programming_language = programming_language
    def get_info(self):
        return f"{self. name} programs in {self.programming_language}"
        
def print_employee(e):
    print(e.get_info())
        
e = Employee('Same')
m = Manager('Jim', 'Engineering')
p = Programmer('Tom', 'Python')

print_employee(e)
print_employee(m)
print_employee(p)