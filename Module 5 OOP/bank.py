class bank:
    def __init__(self, balance):
        self.balance = balance
        self.max_withdrow = 1000
        self.min_withdrow = 10
    
    def get_balance(self):
        return self.balance
    
    def diposite(self, amound):
        self.balance += amound
    
    def withdrow(self, amound):
        if amound < self.min_withdrow:
            print(f'fokira tor tor taka kom')
        elif amound >self.max_withdrow:
            print(f'eto boroluki dekhanor poryojon nai')
        else:
            self.balance -= amound
            print(f'your wihdow is done \n now ur mony is {self.balance}')

taka = bank(5000)
taka.withdrow(1)
taka.withdrow(47777777777)
taka.withdrow(500)