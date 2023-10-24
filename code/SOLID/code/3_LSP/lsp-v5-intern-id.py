class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
    def is_employee_id_valid(self):
        return type(self. employee_id) is int and self. employee_id > 0 # Added complexity 
        
class Intern(Employee):
    def __init__(self, employee_id, name):
        super().__init__(f"I{employee_id}", name)
        
i = Intern(345, "Chuck")
print(i.is_employee_id_valid()) 