class phone:
    manufactured = 'china'

    def __init__(self,onwer,brand,price):
        self.onwer = onwer
        self.brand = brand
        self.price = price
    
my_phone = phone(onwer='Samiul', brand= 'Google', price = 50000)
print(my_phone.onwer, my_phone.brand, my_phone.price)

her_phone = phone(onwer='she my jan', brand= 'Apple', price=120000)
print(her_phone.onwer, her_phone.brand, her_phone.price)

daddy_phone = phone(onwer = 'daddy', brand = 'Nokia', price=2000)
print(daddy_phone.onwer, daddy_phone.brand,daddy_phone.price)