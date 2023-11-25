class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('geu geu geu')

class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meu meu meu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meh meh meh')

rownok = Dog('rownok')
rownok.make_sound()

feroz = cat('feroz')
feroz.make_sound()

tanzim = Goat('tanzim')
tanzim.make_sound()

animals = [rownok, feroz, tanzim] 
for animal in animals:
    animal.make_sound()
