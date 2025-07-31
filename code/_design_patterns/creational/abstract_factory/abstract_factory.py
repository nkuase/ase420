# Interfaces
class AbstractFactory(object):
  def create_button(self): pass
  def create_checkbox(self): pass
  
class AbstractCheckbox(object):
  def select(self): pass

class AbstractButton(object):
  def click(self): pass
  
# GUIFactory implementations  
class MacFactory(AbstractFactory):
  def create_button(self):
    return MacButton()
  def create_checkbox(self):
    return MacCheckbox()
    
class WinFactory(AbstractFactory):
  def create_button(self):
    return WinButton()
  def create_checkbox(self):
    return WinCheckbox()
    
# Button/Checkbox implementations
class MacButton(AbstractButton):
  def click(self):
    print("mac button clicked")
class MacCheckbox(AbstractCheckbox):
  def select(self):
    print("mac checkbox selected")
    
class WinButton(AbstractButton):
  def click(self):
    print("win button clicked")
class WinCheckbox(AbstractCheckbox):
  def select(self):
    print("win checkbox selected")    
    
# Driver    
## Example of cross-platform development
factory = MacFactory()
factory.create_button().click() # Same interface methods 

factory = WinFactory()
factory.create_checkbox().select() # Same interface methods 