class AccountingReport:
    def print_accounting_report(self):
        print ("Accounting")
        print("==========")
        for e in employees: # How to access the employees? 
            print(f"{e.get_full_name()}, ${e.salary}")

class StaffingReport:
    def print_staffing_report(self):
        print("Staffing")
        print("========")
        for e in employees:
            print(f"{e.get_full_name()}, ${e.salary}")