# SRP Violation Example: Class mixes two responsibilities (EmployeeAndStorage)
# (1) Employee domain/business logic, and (2) XML storage persistence
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factor):
        """Calculate raised salary by factor"""
        return self.salary * factor

    def save_as_xml(self):
        """Storage persistence responsibility"""
        with open("emp.xml", "w") as file:
            file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")           
        
