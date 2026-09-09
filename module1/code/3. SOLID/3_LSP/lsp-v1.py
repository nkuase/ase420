class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_year_salary(self):
        print(f"{self.name} year salary ${self.salary * 12}")

e = Employee("Vera", 2000)
e.print_year_salary()