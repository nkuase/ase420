# Interface
class DataSource(object):
  def write_data(self, data): pass
  def read_data(self): pass

# Implementation  
class FileDataSource(DataSource):
  def __main__(self): pass
  def write_data(self, data):
    print(f"I write {data}.")
  def read_data(self):
    print("I read data")
    
# Decorators (added features)
## This decorator contains the common methods and fields
class DataSourceDecorator(DataSource):
  def __init__(self, source):
    self.wrappee = source
  def write_data(self, data):
    self.wrappee.write_data(data)

class EncryptionDecorator(DataSourceDecorator):
  def write_data(self, data):
    print("> Encrypt start")
    self.wrappee.write_data(data)
    print("< Encrypt done")

class CompressionDecorator(DataSourceDecorator):
  def write_data(self, data):
    print("> Compression start")
    self.wrappee.write_data(data)
    print("< Compression done")

# Driver
print("Encrypt")    
source = FileDataSource()
encrypt = EncryptionDecorator(source)
encrypt.write_data("Hello")

print("\nCompress -> Encrypt")
compressed = CompressionDecorator(encrypt)
compressed.write_data("World")
