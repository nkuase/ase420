from employee import Manager, Attendant, Cook, Mechanic
from reporting_v1 import AccountingReport, StaffingReport

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

"""
AccountingReport().print_accounting_report() is the same as
a = AccountingReport()
a.print_accounting_report() 
"""
AccountingReport().print_accounting_report()
print() # empty line
StaffingReport().print_staffing_report()

"""
NameError: "name 'employees' is not defined"
"""
