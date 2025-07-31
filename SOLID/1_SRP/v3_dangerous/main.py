from employee import Employee
from storage import EmployeeStorage

e = Employee("Vera", 2000)
s = EmployeeStorage()
s.save_as_json(e)