class shop :
    
    def __init__(self, buyer):
        self.buyer = buyer
        #instance attribute
        self.cart = []
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehjabin = shop(buyer= 'Mehjabin')
mehjabin.add_to_cart('mecap')
mehjabin.add_to_cart('lipstic')

nisho = shop(buyer= 'Nisho')
nisho.add_to_cart('football')
nisho.add_to_cart('batminton')

print(mehjabin.cart)
print(nisho.cart)