# This is an example of adapter pattern using class adapter
# In this example, we don't need to aggregate the JSONFormat object, instead we inherit from both XMLFormat and XMLFormat

class XMLFormat(object):
  def print_result(self, info):
    print(f"Results in XML '{info}'")

class JSONFormat(object):
  # This new class has a different interface method
  def json_print(self, info):
    print(f"**JSON format** '{info}'")

# This adapter inherits from XMLFile, so it can access the methods in the XMLFile
# It also aggregates the JSONFile object, so it can access the methods in the JSONFile object
class Adapter(XMLFormat, JSONFormat):
  def xml_to_json(self, info):
    print("XML to JSON invoked")
    return f"<<To normal format>> {info}"    
  def print_result(self, info):
    normal = self.xml_to_json(info) # convert XML to normal 
    return self.json_print(normal)

# Driver
## 1. We use XMLFile features
xml = XMLFormat()
xml.print_result('Input')

## 2. We have a request to translate the info into JSON
### 2.2 We make the adapter that uses the JSON component
adapter = Adapter()
### 2.3 We can invoke the adapter method to translate 
adapter.print_result("Input")
