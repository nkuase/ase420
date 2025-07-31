# Introduce Assertion
expense_limit = 10
NULL_EXPENSE = 5
primary_project = None

# Before
## For a portion of code to work correctly, certain conditions or values must be true.
def get_expense_limit1():
  if expense_limit == NULL_EXPENSE or primary_project is None: raise Exception("Wrong assumption!")
  return expense_limit if expense_limit != NULL_EXPENSE else primary_project.get_member_expense_limit()
      
# After
## Replace these assumptions with specific assertion checks.
def get_expense_limit2():
  assert(expense_limit != NULL_EXPENSE and primary_project is not None)
  return expense_limit if expense_limit != NULL_EXPENSE else primary_project.get_member_expense_limit()
  
if __name__ == "__main__":
  print("<Before>")
#  print(get_expense_limit1()) # remove the comment to test this function
  print("<After>")
  print(get_expense_limit2())