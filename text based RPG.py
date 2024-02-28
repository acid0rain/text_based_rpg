# basic rpg game
import random

# assign character name and level
print("Welcome to Ancient Magicks!")
character_name = input("What is your name? ")
character_level = 1
experience = 0

# Accessing individual values
character_stats = [0, 0, 0, 0]

print("Nice to meet you " + character_name)

# loop to validate class input
class_confirmed = False
while not class_confirmed:

    # assign character class
    char_class = input("Choose your class: \nWizard \nWarrior \nRogue \n")
    print("You have chosen the " + char_class + " class")

    # assign stats
    if char_class.lower() == "warrior":
        character_stats = [10, 10, 3, 7]
        class_confirmed = True
    elif char_class.lower() == "rogue":
        character_stats = [5, 10, 5, 10]
        class_confirmed = True
    elif char_class.lower() == "wizard":
        character_stats = [10, 5, 10, 5]
        class_confirmed = True
    else:
        print("Invalid class chosen. Please select either Warrior, Rogue or Wizard")

#display individual stats
health_points = character_stats[0]
strength = character_stats[1]
magic = character_stats[2]
dexterity = character_stats[3]
print("These are your base stats at level 1: \nHP: ", health_points, "\nStrength: ", strength, "\nMagic: ", magic,
      "\nDexterity: ", dexterity) #print base stats

# choose weapon
weapon = False
while not weapon:
    char_weapon = input("Choose your weapon: \nSword \nAxe \nStaff \nBow \n")

    if char_weapon.lower() in ["sword", "axe", "staff", "bow"]:
        print("Nice! You have chosen the " + char_weapon)
        weapon = True
    else:
        print("Weapon does not exist!")


#define level up function
def level_up (character_stats, experience):
    if experience >= 10:
        print("Congratulations you levelled up!")
        character_stats[0] += 2 #add 2 to HP
        character_stats[1] += 2 #add 2 to strength
        character_stats[2] += 2 #add 2 to magic
        character_stats[3] += 2 #add 2 to dex
        print("Your stats have increased. You now have: ")
        print("HP: ",character_stats[0], "\nStrength: ",character_stats[1], "\nMagic: ",character_stats[2], "\nDexterity: ",character_stats[3])
    else:
        print("You have ", experience, "experience.")
#define trap function
def trap(dexterity):
    dodge_chance = 10
    print("You need a +", dodge_chance, "dexterity roll to dodge the trap")
    dodge_roll = random.randrange(10) + dexterity #assign random number between 10
    print("You rolled:", dodge_roll)
    if dodge_roll > dodge_chance:  # calculate chances of dodging trap
        trap_dodged: bool = True
        print("Smooth! You dodged the trap")
        return trap_dodged
    else:
        trap_dodged = False
        print(dodge_chance)
        print("Too slow. The trap got you")
        return trap_dodged


# define functions for each weapon
# sword function
def sword_attack():
    damage = 7 + strength
    hit_chance = 0.7  # 50%chance to hit
    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def axe_attack():
    damage = 10 + strength
    hit_chance = 0.4  # 30%chance to hit
    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def bow_attack():
    damage = 10 + dexterity
    hit_chance = 0.7
    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def staff_attack():
    damage = 13 + magic
    hit_chance = 0.5
    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


# define goblin class and function for attack
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


# begin the game
adventure = input(
    "You are now fully equipped and ready for adventure.\n While travelling you encounter a mysterious looking cave. Do you wish to enter? \nYes \nNo \n").lower()
while adventure == "yes":
    print("A goblin sneaks up behind you and attacks you!")

    # begin fight simulation
    health_points = health_points  # base HP
    goblin = Goblin()  # create instance of goblin to fight

    while health_points > 0 and goblin.health > 0:

        # goblins turn
        goblin_damage = goblin.attack()
        health_points -= goblin_damage
        print("You have", health_points, "health points remaining")
        if health_points <= 0:
            print("Oh no.. the Goblin slayed you. YOU DIED")
            adventure = False
            break

        # players turn
        if char_weapon.lower() == "sword":  # check if weapon sword
            print("You slash with your sword...")
            player_damage = sword_attack()  # call sword attack function
            goblin.health -= player_damage
            print("The goblin has", goblin.health, "health remaining")

            if goblin.health <= 0:
                print("Congratulations! You slayed that goblin bish")
                adventure = False
                break

        elif char_weapon.lower() == "axe":  # call axe attack function
            print("You swing your axe!")
            player_damage = axe_attack()
            goblin.health -= player_damage
            print("The goblin has", goblin.health, "health remaining")

            if goblin.health <= 0:
                print("Congratulations! You slayed that goblin bish")
                adventure = False
                break

        elif char_weapon.lower() == "bow":  # call bow
            print("You fire your bow...")
            player_damage = bow_attack()
            goblin.health -= player_damage
            print("The goblin has", goblin.health, "health remaining")

            if goblin.health <= 0:
                print("Congratulations! You slayed that goblin bish")
                adventure = False
                break

        else:
            print("You cast a spell using your staff!")
            player_damage = staff_attack()
            goblin.health -= player_damage
            print("The goblin has", goblin.health, "health remaining")

            if goblin.health <= 0:
                print("Congratulations! You slayed the goblin.")
                dexterity = dexterity + 2


                adventure = False
                break

if health_points <= 0:
    print("GAME OVER")

else:
    experience = experience + 10 #gain experience
    level_up(character_stats, experience) #call levelup

    print("As you walk over the Goblins dead body you notice a shiny key. Do you wish to take the key?")
    chapter_two = input()
    while chapter_two.lower() == "yes":
        # begin chapter 2 of game
        print("You take the key and keep walking further into the dark chasm of the cave.")
        print("You arrive upon a locked door. You insert the key and slowly turn it")
        print("Your hear the sound of a mechanism turn")
        print("Shit! A trapdoor underneath you swings open")
        # initiate trap
        dodge_trap = trap(dexterity)  # call trap function
        if not dodge_trap:
            print("Game over!")
            break

        else:
            print("You narrowly avoid death")
            break
