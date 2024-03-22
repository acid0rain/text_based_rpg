import random

#----define goblin class and function for attack----#
class Goblin:
    def __init__(self):
        self.health = 50
        self.weakness = "cleave"

    def attack(self):
        damage = 2
        hit_chance = 0.5
        if random.random() <= hit_chance: #returns float between 0 - 1 and compares against hit chance
            print("The goblin attacks you for", damage, "damage!")
            return damage
        else:
            print("The goblin attacked but missed!")
            return 0



#define troll class and attack functions ------
class Troll:
    def __init__(self):
        self.health = 50 #troll health
        self.weakness = "cleave" #weakness to magic

    def attack(self):
        hit_chance = 0.5
        damage = random.randint(3, 7) #random int between 3 and 7
        if random.random() <= hit_chance:
            print("The Troll attacks you for", damage, "damage!")
            return damage
        else:
            print("The Troll attacked but missed..Phew!")
            return 0


