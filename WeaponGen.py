import random
import sqlite3
import json

type = ["Ranged", "Melee"]

def type2gen(type):
    """Generates a random type2 value."""
    if type == "Ranged":
        return random.choice(["Rifle", "Pistol", "Carbine", "Bow", "Crossbow", "Longbow" ,"Launcher"])
    elif type == "Melee":
        return random.choice(["Dagger", "Blade", "Sword", "Duster", "Knuckler", "Fist", "Polearm", "Lance", "Spear", "Warhammer", "Axe", "Greatsword"])

def APgen(type2):

    if type2 == "Launcher":
        return random.choice(["Heavy", "Medium"])

    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        w1 = random.randint(1, 10)
        if w1 > 7:
            return "Heavy"
        elif w1 > 4:
            return "Medium"
        else:
            return random.choice(["Light", "Medium", "None"])

    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        w2 = random.randint(1, 20)
        if w2 == 20:
            return "Heavy"
        elif w2 > 17:
            return "Medium"
        elif w2 > 8:
            return "Light"
        else:
            return random.choice(["None"])

    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        w3 = random.randint(1, 20)
        if w3 > 18:
            return "Heavy"
        elif w3 > 13:
            return "Medium"
        elif w3 > 5:
            return "Light"
        else:
            return random.choice(["None"])



class weapon:
    def __init__(self, type, type2 condition, AP, dmgtype, Speed, Accuracy, Mindmg, Maxdmg, critchance, critdamage, slot, owner):
        self.type = random.choice(type)
        self.type2 = type2gen(self.type)
        self.condition = random.randint(10000,30000)
        self.AP = APgen(self.type2)
        self.dmgtype = type
        self.Speed = Speed
        self.Accuracy = Accuracy
        self.Mindmg = Mindmg
        self.Maxdmg = Maxdmg
        self.critchance = critchance
        self.critdamage = critdamage
        self.slot = slot
        self.owner = owner




