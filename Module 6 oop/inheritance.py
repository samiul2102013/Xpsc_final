#base  class, parent class, common attribute +funtionality class
#derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self,brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop'
class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'learing python and practicing'

class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.dual_sim} brand: {self.brand} price: {self.price} color: {self.color}'
        

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass

my_phone = Phone('sumsung',12000,'blue','china', True)

print(my_phone)