class Employee:
    def __init__(self, last_name, first_name, salary, start_time, end_time):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.start_time = start_time
        self.end_time = end_time
        
    def get_full_name(self):
        return f"{self.last_name},{self.first_name}"
        
class Mechanic(Employee):
    job_title = "Mechanic"
class Attendant(Employee):
    job_title = "Station Attendant"
class Cook(Employee):
    job_title = "Cook"
class Manager (Employee):
    job_title = "Manager"
    
