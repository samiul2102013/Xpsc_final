class kolom:
    #constractor
    def __init__(self, onwer, brand, color, price):
        self.onwer = onwer
        self.brand = brand
        self.color = color
        self.price = price

my_pen = kolom(onwer='samiul', brand = ' matador', color= 'blue', price= 10)
print(my_pen.onwer, my_pen.brand, my_pen.color, my_pen.price)

momens_pen = kolom(onwer= 'Momen', brand= 'matador', color= 'red', price= 4)
print(momens_pen.onwer, momens_pen.brand, momens_pen.color, momens_pen.price)

sp = kolom ( onwer= 'someone',brand= 'something', color= 'green', price=34)
print(sp.onwer, sp.brand, sp.color, sp.price)