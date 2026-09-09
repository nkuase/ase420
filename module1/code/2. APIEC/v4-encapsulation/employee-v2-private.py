class Employee:
    def __init__(self, last_name, first_name, salary):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
    def get_full_name(self):
        return f"{self._last_name},{self._first_name}"

class Mechanic(Employee):
    job_title = "Mechanic"
class Attendant(Employee):
    job_title = "Station Attendant"
class Cook(Employee):
    job_title = "Cook"
class Manager (Employee):
    job_title = "Manager"
    
