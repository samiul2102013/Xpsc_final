class Calculator :
    baran = 'casio MS990'
    def add (self, num1, num2):
        return num1+num2
    
    def deduct (self, num1, num2):
        return num1- num2

    def multipy(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1/num2 
cal = Calculator()
print(cal.add(3,5))
print(cal.deduct(5,2))
print(cal.multipy(3,5))
print(cal.divide(5,3))