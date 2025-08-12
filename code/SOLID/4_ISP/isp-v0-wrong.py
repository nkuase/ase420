from abc import ABCMeta, abstractmethod

class Phone(metaclass=ABCMeta):
    @abstractmethod    
    def call(self, number):""
    @abstractmethod
    def swipe_to_unlock(self):""
        
class IPhone(Phone):
    def call(self, number):
        print(f"Calling Number: {number} from iPhone.")
    def swipe_to_unlock(self):
        print("iPhone is unlocked.")
        
class Nokia2720(Phone):
    def call(self, number):
        print(f" Calling Number: {number} from Nokia 2720.")
    def swipe_to_unlock(self):
        raise NotImplementedError("Nokia 2720 has no touch screen.")
        
i = IPhone()
n = Nokia2720()

i.call('1234')
i.swipe_to_unlock()

n.call('1234')
n.swipe_to_unlock() # Exception as we should not use this interface method