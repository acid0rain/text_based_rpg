import random

#check weak type function
def check_effective(attack_type, weakness, damage):
    if attack_type == weakness:
        damage = damage * 1.3
        print("Your weapon is highly effective against this foe")
    return damage

# ------------ define functions for each weapon --------------
# sword function
def sword_attack(character_stats, weakness):
    attack_type = "slash"
    strength_mod = character_stats[1]
    damage = 7 + strength_mod
    damage = check_effective(attack_type, weakness, damage) #call effective function

    hit_chance = 0.7  # 50%chance to hit
    print("You slash with your sword...")

    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def axe_attack(strength, weakness):
    attack_type = "cleave"
    damage = 10 + strength
    damage = check_effective(attack_type, weakness, damage)  # call effective function

    hit_chance = 0.8  # 30%chance to hit
    print("You swing your axe!")

    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def bow_attack(dexterity, weakness):
    attack_type = "ranged"
    damage = 10 + dexterity
    damage = check_effective(attack_type, weakness, damage)  # call effective function

    hit_chance = 0.7

    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def staff_attack(magic, weakness):
    attack_type = "magic"
    damage = 7 + magic
    damage = check_effective(attack_type, weakness, damage)  # call effective function
    hit_chance = 0.5


    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0

#-----spell casts --------#

def cast_fireball(character_stats, weakness):
    attack_type = "magic"
    damage = 15 + character_stats[2]
    damage = check_effective(attack_type, weakness, damage) #check effectiveness and return new damage
    hit_chance = 1

    if random.random() <= hit_chance:
        print(f"You cast a huge fireball!! It deals:{damage}!")
        return damage
    else:
        print("Bad luck! You missed")
        return 0


def cast_heal(health_points, character_stats):
    health_points = 10 + character_stats[2] #10 plus magic
    print(f"You cast a healing spell, it heals you for {heal_points}")
    health_points += heal_points #add heal points to current HP


def cast_thunderbolt(health_points, character_stats, weakness):
    attack_type = "magic"
    damage = 20 + character_stats[2]
    damage = check_effective(attack_type, weakness, damage)  # check effectiveness and return new damage
    hit_chance = 0.8

    if random.random() <= hit_chance:
        print(f"You summon a thunderbolt from the heavens! It deals:{damage}!")
        return damage
    else:
        print("You try to cast a thunderbolt but instead you end up shocking yourself")
        health_points = health_points - 5
        return 0

#create dictionary mapping each attack and spell function to its weapon / tome

weapon_attacks = {
    "sword": sword_attack,
    "axe": axe_attack,
    "bow": bow_attack,
    "staff": staff_attack,
}

spell_attacks = {
    "fireball": cast_fireball,
    "heal": cast_heal,
    "thunderbolt": cast_thunderbolt

}

