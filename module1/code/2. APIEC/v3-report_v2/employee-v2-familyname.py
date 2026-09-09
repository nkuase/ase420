class Employee:
    def __init__(self, last_name, first_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
class Mechanic(Employee):
    job_title = "Mechanic"
class Attendant(Employee):
    job_title = "Station Attendant"
class Cook(Employee):
    job_title = "Cook"
class Manager (Employee):
    job_title = "Manager"
    
