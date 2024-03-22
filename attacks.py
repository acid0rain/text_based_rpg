import random

# ------------ define functions for each weapon --------------
# sword function
def sword_attack(character_stats, weakness):
    attack_type = "slash"
    strength_mod = character_stats[1]
    damage = 7 + strength_mod
    damage = check_effective(attack_type, weakness, damage) #call effective function

    hit_chance = 0.7  # 50%chance to hit
    attack_type = "slash"
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


def staff_attack(character_stats, weakness):
    attack_type = "magic"
    damage = 13 + magic
    damage = check_effective(attack_type, weakness, damage)  # call effective function
    hit_chance = 0.5


    if random.random() <= hit_chance:
        print("Attack landed! You dealt", damage, "damage.")
        return damage
    else:
        print("Bad luck! You missed")
        return 0

#create dictionary mapping each attack function its weapon

weapon_attacks = {
    "sword":sword_attack,
    "axe": axe_attack,
    "bow": bow_attack,
    "staff": staff_attack
}
