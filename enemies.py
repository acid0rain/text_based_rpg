import random

#----define goblin class and function for attack----#
class Goblin:
    def __init__(self):
        self.health = 50
        self.weakness = "cleave"
        self.xp_gain = 10

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
        self.xp_gain = 20
    def attack(self):
        hit_chance = 0.5
        damage = random.randint(3, 7) #random int between 3 and 7
        if random.random() <= hit_chance:
            print("The Troll attacks you for", damage, "damage!")
            return damage
        else:
            print("The Troll attacked but missed..Phew!")
            return 0



#define giant spider (boss)
class giant_spider:
    def __init__(self):
        self.health = 100
        self.weakness = "magic"
        self.xp_gain = 30

    def attack(self):
        hit_chance = 0.4
        special_attack = 0.2
        damage = random.randint(3, 10)  # random int between 5 and 10 for dmg
        if random.random() <= hit_chance: #returns float between 0 - 1 and compares against hit chance
            print("The Giant Spider slices at you with her claws", damage, "damage!")
            return damage

        elif random.random() <= special_attack:
            damage = damage * 1.5
            print(f"The spider lunges and pierces you with her pincers!")
            print(f"You take {damage} damage!")
        else:
            print("The Giant Spider attacks but misses")
            return 0


