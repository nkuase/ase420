class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_year_salary(self):
        print(f"{self.name} year salary ${self.salary * 12}")

class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name, None) # It hcanges the behavior of the super class

e = Employee("Vera", 2000)
e.print_year_salary()
i = Intern("Jim", 0)
i.print_year_salary() # => TypeError: "unsupported operand type(s) for *: 'NoneType' and 'int'"