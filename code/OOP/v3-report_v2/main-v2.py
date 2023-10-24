# rename employee to either employee-v1 or employee-v2-familyname to run the code
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

employees = [
    Manager ("Vera", "Schmidt", 2000),
    Attendant ("Chuck", "Norris", 1800),
    Attendant ("Samantha", "Carrington", 1800),
    Cook ("Roberto", "Jacketti", 2100),
    Mechanic ("Dave", "Dreißig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic ("Ringo", "Rama", 1900),
    Mechanic ("Chuck", "Rainey", 1800) ,
]

def print_accounting_report():
    print ("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.first_name} {e.first_name}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.first_name} {e.first_name}, ${e.salary}")

print_accounting_report()
print() # empty line
print_staffing_report()

"""
Accounting
==========
Schmidt Schmidt, $2000
Norris Norris, $1800
Carrington Carrington, $1800
Jacketti Jacketti, $2100
Dreißig Dreißig, $2200
River River, $2300
Rama Rama, $1900
Rainey Rainey, $1800

Staffing
========
Schmidt Schmidt, $2000
Norris Norris, $1800
Carrington Carrington, $1800
Jacketti Jacketti, $2100
Dreißig Dreißig, $2200
River River, $2300
Rama Rama, $1900
Rainey Rainey, $1800
"""