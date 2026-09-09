import jsonlibrary

class Employee: 
    def __init__(self, name, salary):
        @jsonserializable
        self.name = name
        @jsonserializable
        self.salary = salary
        
    def raise_salary(self, factor):
        return self.salary * factor
