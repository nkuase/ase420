import jsonlibrary

class EmployeeStorage:
    json_filename = "emp.json"

    def save_as_json(self, employee):
        # Passes the domain Employee directly to the external serialization library
        jsonlibrary.save(self.json_filename, employee)
