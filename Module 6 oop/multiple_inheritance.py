"""
 1. simple inheritance: parent class --> child classs (Gadget-->phone) 
 2. Multi-level inheritance : grandpa -->parent -->child(vechicle --> bus -->ACBus)
 3. multiple inheritance : student(family, Scholl, Sports)
 4. Hybrid : granda -->fatehr,uncle,aunty -->child(father,uncle)
"""
class Family:
    def __init__(self,address) -> None:
        self.address = address

class School:
    def __init__(self,id,level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self,game) -> None:
        self.game = game

class Student(Family,School, Sports):
    def __init__(self, address,id,level,game) -> None:
        Family.__init__(self,address)
        School.__init__(self,id,level)
        Sports.__init__(self, game)

