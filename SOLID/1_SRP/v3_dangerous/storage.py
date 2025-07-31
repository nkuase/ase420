import jsonlibrary

class EmployeeStorage:
    json_filename = "emp.json"
    def save_as_json(self, employee):
        with open(self.json_filename, "w") as file:
            jsonlibrary.save(f"name: {employee. name}, salary: {employee.salary}")
