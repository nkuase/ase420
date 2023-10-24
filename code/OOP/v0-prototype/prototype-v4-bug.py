names = ["Vera", "Chuck", "Samantha", "Roberto", "Dave", "Tina", "Ringo"]
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300, 1900]

count = len (names)
for c in range (count):
    print(f"{names [c]}, ${salaries[c]}")
    
"""
 Vera, $2000
 Chuck, $1800
 Samantha, $1800
 Roberto, $2100
 Dave, $2000 <- ???
 Tina, $2200 <-??? 
 Ringo, $2300 <- ???
"""