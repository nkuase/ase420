# rename employee to either employee-v1 or employee-v2-familyname to run the code
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

def print_accounting_report():
    print ("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.name}, ${e. salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.name}, {e. job_title}")

print_accounting_report()
print() # empty line
print_staffing_report()

"""
Accounting
==========
Vera, $2000
Chuck, $1800
Samantha, $1800
Roberto, $2100
Dave, $2200
Tina, $2300
Ringo, $1900

Staffing
========
Vera, Manager
Chuck, Station Attendant
Samantha, Station Attendant
Roberto, Cook
Dave, Mechanic
Tina, Mechanic
Ringo, Mechanic
"""