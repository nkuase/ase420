class Employee:
    # Equivalent to Java's constructor
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

employees = [
    Employee("Vera", 2000, "Manager"),
    Employee("Chuck", 1800, "Attendant"),
    Employee("Samantha", 1800, "Attendant"),
    Employee("Roberto", 2100, "Cook"),
    Employee("Dave", 2200, "Car Repair"),
    Employee("Tina", 2300, "Car Repair"),
    Employee("Ringo", 1900, "Car Repair")
]
    
for e in employees:
    print(f"{e. name}, ${e.salary}, {e.job_title}") 
        
"""
Vera, $2000, Manager
Chuck, $1800, Attendant
Samantha, $1800, Attendant
Roberto, $2100, Cook
Dave, $2200, Car Repair
Tina, $2300, Car Repair
Ringo, $1900, Car Repair
"""