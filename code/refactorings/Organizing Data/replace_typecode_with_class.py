# Replace Type Code with Class

## Before
class Person(object):
  O = 0; A = 1; B = 2; AB = 3  
  def __init__(self, bloodgroup):
    self.bloodgroup = bloodgroup
### Usage
p = Person(Person.O) # the person has 'O' type
print(p.bloodgroup) # prints 0 

## After
class BloodGroup(object):
  O = 0; A = 1; B = 2; AB = 3  
  def __init__(self, bloodgroup):
    self.bloodgroup = bloodgroup
class Person2(object):
  def __init__(self, bloodgroup):
    self.bloodgroup = bloodgroup
### Usage
p = Person2(BloodGroup.A)
print(p.bloodgroup)