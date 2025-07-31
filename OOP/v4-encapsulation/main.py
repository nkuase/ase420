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
        print(f"{e.get_full_name()}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.get_full_name()}, ${e.salary}")

print_accounting_report()
print() # empty line
print_staffing_report()

"""
Accounting
==========
Vera,Schmidt, $2000
Chuck,Norris, $1800
Samantha,Carrington, $1800
Roberto,Jacketti, $2100
Dave,Dreißig, $2200
Tina,River, $2300
Ringo,Rama, $1900
Chuck,Rainey, $1800

Staffing
========
Vera,Schmidt, $2000
Chuck,Norris, $1800
Samantha,Carrington, $1800
Roberto,Jacketti, $2100
Dave,Dreißig, $2200
Tina,River, $2300
Ringo,Rama, $1900
Chuck,Rainey, $1800
"""