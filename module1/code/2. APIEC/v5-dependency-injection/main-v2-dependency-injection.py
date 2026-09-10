from employee import Manager, Attendant, Cook, Mechanic
from reporting_v2 import AccountingReport, StaffingReport

employees = [
    Manager("Schmidt", "Vera", 2000),
    Attendant("Norris", "Chuck", 1800),
    Attendant("Carrington", "Samantha", 1800),
    Cook("Jacketti", "Roberto", 2100),
    Mechanic("Dreißig", "Dave", 2200),
    Mechanic("River", "Tina", 2300),
    Mechanic("Rama", "Ringo", 1900),
    Mechanic("Rainey", "Chuck", 1800),
]

accounting_report = AccountingReport(employees)
accounting_report.print_accounting_report()

print() # empty line
staffing_report = StaffingReport(employees)
staffing_report.print_staffing_report()

"""
Accounting
==========
Schmidt,Vera, $2000
Norris,Chuck, $1800
Carrington,Samantha, $1800
Jacketti,Roberto, $2100
Dreißig,Dave, $2200
River,Tina, $2300
Rama,Ringo, $1900
Rainey,Chuck, $1800

Staffing
========
Schmidt,Vera, Manager
Norris,Chuck, Station Attendant
Carrington,Samantha, Station Attendant
Jacketti,Roberto, Cook
Dreißig,Dave, Mechanic
River,Tina, Mechanic
Rama,Ringo, Mechanic
Rainey,Chuck, Mechanic
"""
