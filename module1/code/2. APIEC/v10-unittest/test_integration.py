import io
import unittest
from contextlib import redirect_stdout
from employee import Employee
from reporting import AccountingReport


class TestEmployeeReportIntegration(unittest.TestCase):
    def test_salary_report_generation(self):
        employee = Employee("Wonder", "Alice", 5000)
        report = AccountingReport([employee])

        # Use an exact integer multiplier: this integration test checks
        # component collaboration, not floating-point tolerance.
        employee.raise_salary(2)
        output = io.StringIO()
        with redirect_stdout(output):
            report.print_report()

        result = output.getvalue()
        self.assertIn("Wonder,Alice", result)
        self.assertIn("10000", result)


if __name__ == "__main__":
    unittest.main()
