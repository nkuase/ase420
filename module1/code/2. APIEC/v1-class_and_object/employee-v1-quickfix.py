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
    if e.name == "Vera":
        print(f"{e.name}, ${e.salary}, Manager")
    if e.name == "Chuck" or e.name == "Samantha":
        print (f"{e.name}, ${e.salary}, Attendant")
    if e.name == "Roberto":
        print (f"{e.name}, ${e.salary}, Cook")
    if e.name == "Dave" or e. name == "Tina" or e.name == "Ringo":
        print (f"{e.name}, ${e.salary}, Car repair")    
        
"""
Vera, $2000, Manager
Chuck, $1800, Attendant
Samantha, $1800, Attendant
Roberto, $2100, Cook
Dave, $2200, Car repair
Tina, $2300, Car repair
Ringo, $1900, Car repair
"""