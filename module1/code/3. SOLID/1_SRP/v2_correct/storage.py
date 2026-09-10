import json

class EmployeeStorage:
    json_filename = "emp.json"

    def save_as_json(self, employee):
        data = {
            "name": employee.name,
            "salary": employee.salary
        }
        with open(self.json_filename, "w") as file:
            json.dump(data, file, indent=2)
