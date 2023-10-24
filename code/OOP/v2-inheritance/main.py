from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
    
"""
Vera, $2000, Manager
Chuck, $1800, Station Attendant
Samantha, $1800, Station Attendant
Roberto, $2100, Cook
Dave, $2200, Mechanic
Tina, $2300, Mechanic
Ringo, $1900, Mechanic
"""    