class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_year_salary(self):
        print(f"{self.name} year salary ${self.salary * 12}")
    def promote(self):
        print("Promote Employee")

class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name, None) # It hcanges the behavior of the super class
    def promote(self):
        raise NotImplementedError("Interns cannot be promoted")

def promote_employee(e):
    e.promote() # crashes when e is an intern

e = Employee("Vera", 2000)
e.print_year_salary()
i = Intern("Jim", 0)

promote_employee(e) # OK
promote_employee(i) # Crash