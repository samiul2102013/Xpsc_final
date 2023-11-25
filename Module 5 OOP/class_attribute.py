class shop :
    #class attribute
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)

mehzaben = shop('mehejaben')
mehzaben.add_to_cart('shoes')
mehzaben.add_to_cart('mecap')
mehzaben.add_to_cart('lipstik')

nisho = shop('nisho')
nisho.add_to_cart('football')
nisho.add_to_cart('cricket ball')
nisho.add_to_cart('jersi')

print(shop.cart)

print(mehzaben.cart)

print(nisho.cart)