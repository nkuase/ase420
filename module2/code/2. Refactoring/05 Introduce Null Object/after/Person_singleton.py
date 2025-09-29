from Label_singleton import Label

class Person:
    """Person class using null object pattern with factory method"""
    
    def __init__(self, name, mail=None):
        self._name = name
        self._mail = mail if mail is not None else Label.new_null()
    
    def display(self):
        self._name.display()
        self._mail.display()
    
    def __str__(self):
        return f"[ Person: name={self._name} mail={self._mail} ]"
