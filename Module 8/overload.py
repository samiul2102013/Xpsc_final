class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    
    def __gt__(self, other):
        return self.age > other.age

players = [
    Cricketer('Sakib', 38, 68, 91),
    Cricketer('Mushfiq', 36, 55, 82),
    Cricketer('Mustafiz', 27, 69, 86),
    Cricketer('Riyad', 39, 72, 92)
]

youngest_player = players[0]

for player in players:
    if player < youngest_player:
        youngest_player = player

print("Youngest player:", youngest_player.name)
