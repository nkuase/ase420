class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
    def is_employee_id_valid(self):
        return self. employee_id > 0
        
class Intern(Employee):
    def __init__(self, employee_id, name):
        super().__init__(employee_id, name)
        
i = Intern(345, "Chuck")
print(i.is_employee_id_valid()) 