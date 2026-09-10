from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
from shift_v1 import MorningShift, AfternoonShift

employees = [
    Manager("Schmidt", "Vera", 2000, MorningShift()),
    Attendant("Norris", "Chuck", 1800, MorningShift()),
    Attendant("Carrington", "Samantha", 1800, AfternoonShift()),
    Cook("Jacketti", "Roberto", 2100, MorningShift()),
    Mechanic("Dreissig", "Dave", 2200, MorningShift()),
    Mechanic("Rivers", "Tina", 2300, MorningShift()),
    Mechanic("Rama", "Ringo", 1900, AfternoonShift()),
    Mechanic("Rainey", "Chuck", 1800, AfternoonShift()),
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()
