class Player:
    def __init__ (self):
        self.name = input("Entrez le nom de votre personnage ")
        self.xp = 0
        self.level = 1


    def presentation(self):
        print(f"I'm the player {self.name} and I'm level {self.level}.")
        print(f"for the moment i only have {self.xp} pts of XP but in ")

    def gain_xp(self,amount):
        self.xp = self.xp + amount
        print(f"You earned {amount} pts of xp")
        if self.xp >= 

player1 = Player()
player1.presentation()



while player1.xp >= 0 :
    x = player1.level - 1
    player1.level = player1.level + 1
    player1.xp = player1.xp - (500 * (1.2) ** x)
    x = x+1
    print(f"{player1.xp}")
    player1.presentation()