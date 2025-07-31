# interfaces
class Factory(object):
  @staticmethod
  def create_button(): pass

class Product(object):
  def render(self): pass
  def on_click(self): pass
  
# Dialog implementation  
class WindowsDialog(Factory):
  @staticmethod
  def create_button():
    return WindowsButton()
    
class WebDialog(Factory):
  @staticmethod
  def create_button():
    return HTMLButton()
    
# Button implementation
class WindowsButton(Product):
  def render(self):
    print("rendering in Windows Button")
class HTMLButton(Product):
  def render(self):
    print("rendering in HTML Button")    

# Driver
## We don't need to use new operator (or equivalent) anymore
ok_button = WindowsDialog.create_button()    
ok_button.render()
ok_button = WebDialog.create_button()    
ok_button.render()