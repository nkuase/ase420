from employee import Manager, Attendant, Cook, Mechanic
from reporting_v2 import AccountingReport, StaffingReport

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

accounting_report = AccountingReport(employees)
accounting_report.print_accounting_report()

print() # empty line
staffing_report = StaffingReport(employees)
staffing_report.print_staffing_report()

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