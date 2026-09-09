class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
# job_title is a class variable (without self), not instance variable        
# Shared between all instances of the class.
# Every Mechanic has job_title = "Mechanic"
class Mechanic(Employee):
    job_title = "Mechanic"
class Attendant(Employee):
    job_title = "Station Attendant"
class Cook(Employee):
    job_title = "Cook"
class Manager (Employee):
    job_title = "Manager"
    
