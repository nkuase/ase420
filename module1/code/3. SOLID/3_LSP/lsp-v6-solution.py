# LSP Refactored Solution:
#
# Root Cause: The Employee base class enforced salary calculation, promotion,
# and integer ID contracts onto all subclasses. Interns cannot fulfill these contracts.
#
# Two valid architectural solutions:
# 1. Contract Redesign: Redesign the hierarchy so Employee only declares universal
#    worker behavior (name, identity), while Salaried and Promotable become separate roles/interfaces.
# 2. Disconnecting Inheritance: When regular employees and interns have distinct lifecycles
#    and no shared polymorphic dispatch is required, model them as independent classes.

# --- Option 2: Independent Classes (Disconnecting Inheritance) ---

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def is_employee_id_valid(self):
        # type() is int ensures bool is rejected (since bool is a subclass of int)
        return type(self.employee_id) is int and self.employee_id > 0

    def print_year_salary(self):
        print(f"{self.name} year salary ${self.salary * 12}")

    def promote(self):
        print(f"Promoted {self.name}")

class Intern:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Intern: {self.name}"

# --- Usage Demonstrating Preservation of Contracts ---

e = Employee(101, "Vera", 2000)
print(f"Employee ID valid: {e.is_employee_id_valid()}")
e.print_year_salary()
e.promote()

i = Intern("Jim")
print(i.get_info())
