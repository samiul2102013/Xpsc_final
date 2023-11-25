class Student:
    def __init__(self, name) -> None:
        self.name = name

class Address(Student):
    def __init__(self, name, address) -> None:
        self.address = address
        super().__init__(name)

class Id(Address):
    def __init__(self, name, address,id) -> None:
        self.id = id
        super().__init__(name, address)

class Batch(Id):
    def __init__(self, name, address, id,batch) -> None:
        self.batch = batch
        super().__init__(name, address, id)
    
    def __repr__(self) -> str:
        return f'name: {self.name} id: {self.id} address: {self.address} batch: {self.batch}'

stu = Batch('samiul','Mymensing', 13, 11)
print(stu)