class Shopping:
    cart = [] # class attribute or static attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
    def purches(self, item, price, amound):
        remaning = amound = price
        print(f'buyiing: {item} for price: {price} and remainging: {remaning}')

    @classmethod
    def hudai_dekhi(self,item):
        print(f'kinina dekhi',item)
    
    @staticmethod
    def multiply(a, b):
        print(a*b)

basundara = Shopping('bau','popular')
#basundara.purches('lungi',5,23) #when it is in a object is instace class where three argument enough
#Shopping.purches('a',2,3,4) #class method thats why it take one more argument
Shopping.hudai_dekhi('s')

#static method
Shopping.multiply(2,3)
basundara.multiply(3,7)