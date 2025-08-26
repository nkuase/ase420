names = ["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina", "Ringo"]
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300]

count = len (names)
for c in range (count):
    print (f" {names [c]}, ${salaries[c]}")
    
"""
Traceback (most recent call last):
  File "/Users/smcho/Desktop/-Now/ASE420/code/introduction_example/code/prototype/v3-bug.py", line 6, in <module>
    print (f" {names [c]}, ${salaries[c]}")
IndexError: list index out of range
"""