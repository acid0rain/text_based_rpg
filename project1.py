#basic rpg game
import random

#assign character name and level
print("Welcome to Ancient Magicks!")
character_name = input("What is your name? ")
character_level = 1
print("Nice to meet you "+character_name)

#loop to validate class input
class_confirmed = False
while not class_confirmed:

    #assign character class
    char_class = input("Choose your class: \nWizard \nWarrior \nRogue \n")
    print("You have chosen the " + char_class + " class")

    #assign stats
    if char_class.lower() == "warrior":
        health_points = "10"
        strength = "10"
        magic = "5"
        dexterity = "5"
        class_confirmed = True
    elif char_class.lower() == "rogue":
        health_points = "5"
        strength = "10"
        magic = "5"
        dexterity = "10"
        class_confirmed = True
    elif char_class.lower() == "wizard":
        health_points = "5"
        strength = "5"
        magic = "10"
        dexterity = "10"
        class_confirmed = True
    else:
        print("Invalid class chosen. Please select either Warrior, Rogue or Wizard")
print("These are your base stats at level 1: \nHP: "+health_points + "\nStrength: " + strength + "\nMagic: " + magic + "\nDexterity: " + dexterity)

#choose weapon
weapon = False

while not weapon:
    char_weapon = input("Choose your weapon: \nSword \nAxe \nDagger \nStaff \nBow \n")

    if char_weapon.lower() in ["sword", "axe", "dagger", "staff", "bow"]:
        print("Nice! You have chosen the " + char_weapon)
        weapon = True
    else:
        print("Weapon does not exist!")

#define functions for each weapon
#sword function
def sword_attack():
    damage = 10
    hit_chance = 0.5 #50%chance to hit
    if random.random() <= hit_chance:
        print ("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print ("Bad luck! You missed")
        return 0


#define goblin class and function for attack
class Goblin:
    def __init__(self):
        self.health = 50

    def attack(self):
        damage = 2
        hit_chance = 0.5
        if random.random() <= hit_chance:
            print("The goblin attacks you for", damage, "damage!")
            return damage
        else:
            print("The goblin attacked but missed!")
            return 0


#begin the game
adventure = input("You are now fully equipped and ready for adventure.\n While travelling you encounter a mysterious looking cave. Do you wish to enter? \nYes \nNo \n").lower()
while adventure == "yes":
    print("A goblin sneaks up behind you and attacks you!")

    #begin fight simulation
    health_points = 10 #base HP
    goblin = Goblin() #create instance of goblin to fight

    while health_points > 0 and goblin.health > 0:

        #goblins turn
        goblin_damage = goblin.attack()
        health_points -= goblin_damage
        print("You have", health_points, "health points remaining")
        if health_points <= 0:
            print("Oh no.. the Goblin slayed you. YOU DIED")
            adventure = False
            break

        #players turn
        player_damage = sword_attack()
        goblin.health -= player_damage
        print("The goblin has", goblin.health, "health remaining")

        if goblin.health <= 0:
            print("Congratulations! You slayed that goblin bish")
            adventure = False
            break

