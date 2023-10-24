from employee import Manager, Attendant, Cook, Mechanic
from reporting_v1 import AccountingReport, StaffingReport, ScheduleReport
import datetime

employees = [
    Manager("Vera", "Schmidt", 2000, datetime.time(8,00), datetime.time(14,00)),
    Attendant("Chuck", "Norris", 1800, datetime.time(8,00), datetime.time (14,00)),
    Attendant("Samantha", "Carrington", 1800, datetime.time(12,00), datetime.time (20,00)),
    Cook("Roberto", "Jacketti", 2100, datetime.time (8,00) , datetime.time(14,00)),
    Mechanic("Dave", "Dreißig", 2200, datetime.time(8,00), datetime.time (14,00)),
    Mechanic("Tina", "River", 2300, datetime.time(8,00) , datetime.time(14,00)),
    Mechanic("Ringo", "Rama", 1900, datetime.time(12,00), datetime.time (20,00)),
    Mechanic("Chuck", "Rainey", 1800, datetime.time(12,00), datetime.time (20,00)),
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]

for report in reports:
    report.print_report()
    print()

"""
...

Staffing
========
Vera,Schmidt, 08:00 to 14:00
Chuck,Norris, 08:00 to 14:00
Samantha,Carrington, 12:00 to 20:00
Roberto,Jacketti, 08:00 to 14:00
Dave,Dreißig, 08:00 to 14:00
Tina,River, 08:00 to 14:00
Ringo,Rama, 12:00 to 20:00
Chuck,Rainey, 12:00 to 20:00
"""