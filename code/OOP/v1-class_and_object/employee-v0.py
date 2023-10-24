class Employee:
    # Equivalent to Java's constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Instantiation, but no need to use "new"        
# self in the __init__ method is referencing the "e" object
e = Employee("Vera", 2000)

employees = [
    Employee("Vera", 2000),
    Employee("Chuck", 1800),
    Employee("Samantha", 1800),
    Employee("Roberto", 2100),
    Employee("Dave", 2200),
    Employee("Tina", 2300),
    Employee("Ringo", 1900)
]
for e in employees:
    print(f"{e. name}, ${e.salary}")
    
"""
Vera, $2000
Chuck, $1800
Samantha, $1800
Roberto, $2100
Dave, $2200
Tina, $2300
Ringo, $1900
"""