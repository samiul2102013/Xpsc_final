class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'learing python and practicing'

class Phone:
    def __init__(self, brand, price, color,memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    
    def run(self):
        return f'phone tipa tipi kore'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'

class Camera:
    def __init__(self,brand, price,color,pixel) -> None:
        self.brand = brand
        self.price = price 
        self.color = color
        self.pixel = pixel
    
    def run(self):
        pass

    def change_lens(self):
        pass