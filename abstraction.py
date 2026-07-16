#abstraction    @=decarater
from abc import ABC,abstractmethod
class Phpay(ABC):
    @abstractmethod
    def Pay(self):
        print("paying using phpay")
    def paying(self):
        pass

class Gpay(Phpay):
    def Pay(self):
        print("this is using Gpay")
    def Paying(self):
        print("this is john")
        
obj=Gpay()
obj.Pay()