class AccountingReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list
        
    def print_accounting_report(self):
        print ("Accounting")
        print("==========")
        for e in self._emp_list: 
            print(f"{e.get_full_name()}, ${e.salary}")

class StaffingReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list
            
    def print_staffing_report(self):
        print("Staffing")
        print("========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")