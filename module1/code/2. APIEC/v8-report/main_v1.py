from employee import Manager, Attendant, Cook, Mechanic
from reporting_v1 import AccountingReport, StaffingReport, ScheduleReport
import datetime

employees = [
    Manager("Schmidt", "Vera", 2000, datetime.time(8, 0), datetime.time(14, 0)),
    Attendant("Norris", "Chuck", 1800, datetime.time(8, 0), datetime.time(14, 0)),
    Attendant("Carrington", "Samantha", 1800, datetime.time(12, 0), datetime.time(20, 0)),
    Cook("Jacketti", "Roberto", 2100, datetime.time(8, 0), datetime.time(14, 0)),
    Mechanic("Dreißig", "Dave", 2200, datetime.time(8, 0), datetime.time(14, 0)),
    Mechanic("River", "Tina", 2300, datetime.time(8, 0), datetime.time(14, 0)),
    Mechanic("Rama", "Ringo", 1900, datetime.time(12, 0), datetime.time(20, 0)),
    Mechanic("Rainey", "Chuck", 1800, datetime.time(12, 0), datetime.time(20, 0)),
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

Schedule
========
Schmidt,Vera, 08:00 to 14:00
Norris,Chuck, 08:00 to 14:00
Carrington,Samantha, 12:00 to 20:00
Jacketti,Roberto, 08:00 to 14:00
Dreißig,Dave, 08:00 to 14:00
River,Tina, 08:00 to 14:00
Rama,Ringo, 12:00 to 20:00
Rainey,Chuck, 12:00 to 20:00
"""
