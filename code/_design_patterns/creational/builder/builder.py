# interface
class Builder(object):
  def set_engine(self): pass
  def set_trip_computer(self): pass
  def get_result(self): pass

class Product(object): pass
  
# implementations
class CarBuilder(Builder):
  def set_engine(self):
    print("Setting an engine in a car")
  def set_trip_computer(self):
    print("Setting a trip computer in a car")
  def get_result(self):
    return Car()
    
class CarManualBuilder(Builder):
  def set_engine(self):
    print("Making an engine maunal")
  def set_trip_computer(self):
    print("Making a trip computer manual")
  def get_result(self):
    return Manual()
    
# Final Product
class Car(Product):
  def __init__(self):
    print("car is made")
class Manual(Product):
  def __init__(self):
    print("Manual is made")
    
# Driver
car_builder = CarBuilder()
car_builder.set_engine()
car_builder.set_trip_computer()
car_builder.get_result()

## Same interface methods
car_builder = CarManualBuilder()
car_builder.set_engine()
car_builder.set_trip_computer()
car_builder.get_result()