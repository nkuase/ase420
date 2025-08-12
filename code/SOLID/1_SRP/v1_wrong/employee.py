# TooManyThingsNameProblem
class Employee: # EmployeeAndStorageAndReporting
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def raise_salary(self, factor):
        return self.salary * factor
    def save_as_xml(self):
        with open("emp.xml", "w") as file:
            file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")
    def print_employee_report(self):
        pass           
        
