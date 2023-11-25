class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self. height = height
        self.weight = weight
    
    def eat(self):
        print('vat mangso polau korma khai')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('ami sakib')

    def exercise(self):
        print('ami exercise kori')
    
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.age * other.age
    
sakib = Cricketer('kakib',38, 68, 91,'ind')
mushi = Cricketer('mushi',38,65,70,'bd')
sakib.eat()
sakib.exercise()
# plus sign overload
print(45 + 64)
print('sakib' + 'Rakib')
print([12,34] + [56,43,64])
""" here sakib and mushi are object they can't be added using a + sing
so in Cricketer class the plus(+) sing is overloaded that  means when 
a + sing added this plus will return two age  """
print(sakib + mushi)
print(sakib * mushi)