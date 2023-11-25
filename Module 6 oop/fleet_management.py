class company:
    def __init__(self,name, address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.diriver = []
        self.counter = []
        self.manager = []
        self.supervisors = []

class Driver:
    def __init__(self,name, license, age) -> None:
        self.name = name
        self.licence = license
        self.age = age

class passenger :
    pass

class supervisor:
    pass

red_mea = Driver('a',123,32)