from abc import ABCMeta, abstractmethod

class PhoneCall(metaclass=ABCMeta):
    @abstractmethod    
    def call(self, number):""
    
class Touch(metaclass=ABCMeta):    
    @abstractmethod
    def swipe_to_unlock(self):""
        
class IPhone(PhoneCall, Touch):
    def call(self, number):
        print(f"Calling Number: {number} from iPhone.")
    def swipe_to_unlock(self):
        print("iPhone is unlocked.")
        
class Nokia2720(PhoneCall):
    def call(self, number):
        print(f"Calling Number: {number} from Nokia 2720.")
        
i = IPhone()
n = Nokia2720()

i.call('1234')
i.swipe_to_unlock()

n.call('1234')
