class shoping:

    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self, amound):
        total =0
        for item in self.cart:
            total += item['quantity'] * item['price']
        
        if amound < total :
            print("you need more money")
        else :
            amound -= total
            print('take your product now your money {amound}')
    

swapan = shoping('Alan Swapon')
swapan.add_to_cart('alu', 20,5)
swapan.add_to_cart('peyaj', 10, 5)
swapan.add_to_cart('morij',90,1)

print(swapan.checkout(1000))
