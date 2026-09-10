import jsonlibrary

# Dedicated serialization DTO/adapter holding framework decorators
@jsonlibrary.jsonserializable
class JsonEmployee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeStorage:
    json_filename = "emp.json"

    def save_as_json(self, employee):
        # Decoupled: converts domain Employee into JsonEmployee DTO.
        # Employee remains untouched and completely free of jsonlibrary dependencies!
        json_emp = JsonEmployee(employee.name, employee.salary)
        jsonlibrary.save(self.json_filename, json_emp)

