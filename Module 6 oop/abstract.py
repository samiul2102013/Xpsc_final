from abc import ABC, abstractmethod
# abc -> abstract base class
class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print('i need food')
    @abstractmethod
    def move(self):
        print('sob gula murgi ho')

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
    def eat(self):
        print('hey mama i am eating banana')
    def move(self):
        return super().move()

leyka = Monkey('lucky')
leyka.eat()
leyka.move()