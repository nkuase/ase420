from employee import Manager, Attendant, Cook, Mechanic
from reporting_v1 import AccountingReport, StaffingReport

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