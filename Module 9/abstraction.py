"""
1. a object form a class who contain abstracmethod can not be maked
2. it decleaced to just use it as a model
3. it show funtion but hide implementation detail
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, num1, num2) -> None:
        super().__init__(num1, num2)
    
    def area(self):
        print(self.num1*self.num2)

t1 = Triangle(10,20)
t1.area()