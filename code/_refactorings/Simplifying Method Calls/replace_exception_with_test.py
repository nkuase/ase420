# Replace Exception with Test

# Before
## You throw an exception in a place where a simple test would do the job?

def get_value_for_period1(value, period_number):
  try:
    return value[period_number]
  except Exception as e:
    return -1
        
# After
## Replace the exception with a condition test.
def get_value_for_period2(value, period_number):
  if period_number >= len(value): return -1
  return values[period_number]
  
if __name__ == "__main__":
  print("<Before>")
  print(get_value_for_period1([10, 20, 30], 20))
  print("<After>")
  print(get_value_for_period2([10, 20, 30], 20))
