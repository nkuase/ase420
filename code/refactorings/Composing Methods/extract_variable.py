# Extract Variable
platform = "mac"
browser = "ie"
size = 100

# Before
def extract_variable1():
  if platform.upper().find("MAC") > -1 and browser.upper().find("IE") > -1:
    print('MAC & IE')

# After
def extract_variable2():
  def isMacOs(): return platform.upper().find("MAC") > -1
  def isIE(): return browser.upper().find("IE") > -1

  if isMacOs() and isIE():
    print('MAC & IE')

if __name__ == "__main__":    
  extract_variable1()
  extract_variable2()    
