class Player:
    def __init__ (self,name,level):
        self.name = name
        self.xp = 0
        self.level = level


    def presentation(self):
        print(f"I'm the player {self.name} and I'm level {self.level}")

level = 1

player1 = Player(name = "loris", level = level)

xp = 0
x = 0
while xp > 0 :
    player1.level = player1.level + 1
    xp = xp - (500 * (1.2) ** x)
    x = x+1
    print(f"{xp}")
    player1.presentation()

print("the fuck")

