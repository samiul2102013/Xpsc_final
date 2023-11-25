# encapsulation --> hide inmplementation detail
class Bank:
    def __init__(self,holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #public attribute: all class can access
        self._barnce = 'banani 11' #protected attribute: can be access from derived class
        self.__balance= initial_deposit # private: just own classs can access
    
    def diposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

rafsun = Bank('choto bai',10000)
rafsun.diposite(50000)
print(rafsun.get_balance())
print(rafsun._barnce)
