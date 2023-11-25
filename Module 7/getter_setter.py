class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money
    def get_money(self):
        return self.__money
        
    @property
    # using @propery now its a getter attribute it can just read
    def moy(self):
        return self.__money
    
    @moy.setter
    #now moy function can read for the setter method
    def moy(self,value):
        self.__money += value

samsu = User('kupa', 23, 1200)
print(samsu.name,samsu._age)
#print(samsu.__money) 
print(samsu.get_money())
# to use function as attribute @property key word nedd to use
print(samsu.moy)
samsu.change_selary = 1
print(samsu.moy)

