import random
import sqlite3
import json
from namegen import generateWname

type = ["Ranged", "Melee"]
damagetypes = ["Kinetic", "Heat", "Energy", "Projectile", "Electric", "Cold", "Acid", "Explosive", "Exotic",
                             "Dark", "Sonic", "Water", "Divine"]

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

    elif type2 == "Duster" or "Knuckler" or "Fist":
        w4 = random.randint(1, 20)
        if w4 > 18:
            return "Heavy"
        elif w4 > 13:
            return "Medium"
        elif w4 > 5:
            return "Light"
        else:
            return random.choice(["None"])

def conditiongen(provrating):
    random.randint(10000,30000)

def speedgen(type2, AP):
    """Generates a random speed value based on type2 and AP."""

    if type2 == "Launcher":
        typemultiplier = random.randint(40, 50)
    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        typemultiplier = random.randint(17, 20)
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        typemultiplier = random.randint(14, 16)
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        typemultiplier = random.randint(9, 13)
    elif type2 == "Duster" or "Knuckler" or "Fist":
        typemultiplier = random.randint(5, 10)
    if AP == "Heavy":
        APmultiplier = random.randint(17, 20)
    elif AP == "Medium":
        APmultiplier = random.randint(14, 16)
    elif AP == "Light":
        APmultiplier = random.randint(9, 13)
    elif AP == "None":
        APmultiplier = random.randint(5, 10)

    TM = typemultiplier * 2
    APM = APmultiplier * 2

    provspeed = float(((TM + APM) * 3) / 60)

    return provspeed

'''def accuracygen(type2):
    """Generates a random accuracy value based on type2."""
    if type2 == "Launcher":
        return random.randint(1, 10)
    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return random.randint(15, 40)
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return random.randint(30, 60)
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return random.randint(40, 70)
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return random.randint(50, 80)'''

def maxdamgen(type2):
    """Generates a random minimum damage value based on type2."""
    if type2 == "Launcher":
        return random.randint(300, 1200)
    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return random.randint(350, 800)
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return random.randint(250, 650)
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return random.randint(250, 650)
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return random.randint(175, 350)

def minddamgen(type2, maxdam):
    """Generates a random maximum damage value based on type2."""
    if type2 == "Launcher":
        return random.randint(290, maxdam)
    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return random.randint(210, maxdam)
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return random.randint(160, maxdam)
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return random.randint(130, maxdam)
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return random.randint(90, maxdam)

def critchancegen(type2, maxdam):
    """Generates a random critical chance value based on type2, maxdam, and speed."""
    if type2 == "Launcher":
        if maxdam > 900:
            return random.randint(0, 5)
        elif maxdam > 600:
            return random.randint(0, 4)
        else:
            return random.randint(0, 3)

    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        if maxdam > 650:
            return random.randint(0, 12)
        elif maxdam > 500:
            return random.randint(0, 10)
        else:
            return random.randint(0, 6)

    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        if maxdam > 400:
            return random.randint(0, 17)
        elif maxdam > 290:
            return random.randint(0, 15)
        else:
            return random.randint(0, 10)

    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        if maxdam > 400:
            return random.randint(0, 25)
        elif maxdam > 290:
            return random.randint(0, 17)
        else:
            return random.randint(0, 14)

    elif type2 == "Duster" or "Knuckler" or "Fist":
        if maxdam > 290:
            return random.randint(0, 35)
        elif maxdam > 190:
            return random.randint(0, 25)
        else:
            return random.randint(0, 20)
def criticalmgen(critchance):
    """Generates a random critical damage value based on critchance."""
    if critchance > 0:
        return random.randint(5, 30)
    else:
        return 0

def slotgen(type2):
    """Generates a random slot value based on type2."""
    if type2 == "Launcher":
        return "Two Handed"
    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return "Two Handed"
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return "Two Handed"
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return random.choices(["Primary", "Secondary"],weights=[80,20], k=1)[0]
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return random.choices(["Primary", "Secondary"],weights=[60,40], k=1)[0]

def ratinggen(type2, Maxdmg, Mindmg, Speed, Accuracy, critchance, critdamage):
    if type2 == "Launcher":
        return int(((Maxdmg / 1200) + (Mindmg / 1200) + ((100 - Speed) / 94.3) + (Accuracy / 50) +
                    (critchance / 5) + (critdamage / 30)) / 6 * 100)
    if type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return int(((Maxdmg / 800) + (Mindmg / 800) + ((100 - Speed) / 97.8) + (Accuracy / 50) +
                    (critchance / 12) + (critdamage / 30)) / 6 * 100)
    if type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return int(((Maxdmg / 650) + (Mindmg / 650) + ((100 - Speed) / 98.1) + (Accuracy / 50) +
                    (critchance / 17) + (critdamage / 30)) / 6 * 100)
    if type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return int(((Maxdmg / 650) + (Mindmg / 650) + ((100 - Speed) / 98.6) + (Accuracy / 50) +
                    (critchance / 25) + (critdamage / 30)) / 6 * 100)
    if type2 == "Duster" or "Knuckler" or "Fist":
        return int(((Maxdmg / 350) + (Mindmg / 350) + ((100 - Speed) / 99) + (Accuracy / 50) +
                    (critchance / 35) + (critdamage / 30)) / 6 * 100)

    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        return int(((Maxdmg + Mindmg) / 2) * (Speed * 10) * (Accuracy * 5) * (critchance * 2) * (critdamage / 100))
    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        return int(((Maxdmg + Mindmg) / 2) * (Speed * 10) * (Accuracy * 5) * (critchance * 2) * (critdamage / 100))
    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        return int(((Maxdmg + Mindmg) / 2) * (Speed * 10) * (Accuracy * 5) * (critchance * 2) * (critdamage / 100))
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return int(((Maxdmg + Mindmg) / 2) * (Speed * 10) * (Accuracy * 5) * (critchance * 2) * (critdamage / 100))

def specialgen(type2):
    """Generates a random special value based on type2."""
    luck = random.randint(1, 10)
    if luck < 8:
        return "None"
    elif type2 == "Launcher":
        return random.choice(["Laser Targetting", "Expanded Blast Radius"])
    elif type2 == "Rifle" or "Longbow":
        return random.choice(["Snipershot", "Headshot", "Mindblast"])
    elif type2 == "Warhammer" or "Axe" or "Greatsword":
        return random.choice(["Cleave", "Heavy Blow", "Hilt Smash"])
    elif type2 == "Carbine" or "Bow":
        return random.choice(["Rapid Fire", "Piercing Shot", "Explosive Projectile"])
    elif type2 == "Polearm" or "Lance" or "Spear":
        return random.choice(["Charge", "Impale", "Polearm Sweep"])
    elif type2 == "Pistol" or "Crossbow":
        return random.choice(["Quickdraw", "Silencer", "Stealth Shot"])
    elif type2 == "Dagger" or "Blade" or "Sword":
        return random.choice(["Backstab", "Parry", "Riposte"])
    elif type2 == "Duster" or "Knuckler" or "Fist":
        return random.choice(["Quick Jab", "Heavy Punch", "Fist Slam"])

class weapon:
    def __init__(self, type, type2, condition, AP, dmgtype, Speed, Accuracy, Mindmg, Maxdmg, critchance, critdamage, slot, special, owner, name, rating):
        self.type = type if type is not None else random.choice(["Ranged", "Melee"])
        self.type2 = type2 if type2 is not None else type2gen(self.type)


        self.AP = AP if AP is not None else APgen(self.type2)
        self.dmgtype = dmgtype if dmgtype is not None else random.choice(damagetypes)
        self.Speed = Speed if Speed is not None else speedgen(self.type2,self.AP)
        self.Accuracy = Accuracy if Accuracy is not None else random.randint(30,50)
        self.Maxdmg = Maxdmg if Maxdmg is not None else maxdamgen(self.type2)
        self.Mindmg = Mindmg if Mindmg is not None else minddamgen(self.type2,self.Maxdmg)

        self.critchance = critchance if critchance is not None else critchancegen(self.type2, self.Maxdmg)
        self.critdamage = critdamage if critdamage is not None else criticalmgen(self.critchance)
        self.slot = slot if slot is not None else slotgen(self.type2)
        self.condition = condition if condition is not None else random.randint(10000,30000)
        self.owner = owner if owner is not None else "player1"
        self.rating = rating if rating is not None else ratinggen(self.type2, self.Maxdmg, self.Mindmg, self.Speed, self.Accuracy, self.critchance, self.critdamage)

        self.special = special if special is not None else specialgen(self.type2)
        self.name = name if name is not None else generateWname(self.type2, self.AP, self.rating, self.slot)

def generateweapon():
    """Generates a random weapon object."""
    return weapon(None, None, None, None, None, None, None,
                  None, None, None, None, None, None, None,
                  None, None)


def printweapon(weapon_item):
    """Prints the weapon object."""
    print("Weapon Name: " + weapon_item.name)
    print("Weapon Type: " + weapon_item.type)
    print("Weapon Type2: " + weapon_item.type2)
    print("Weapon AP: " + weapon_item.AP)
    print("Weapon Damage Type: " + weapon_item.dmgtype)
    print("Weapon Speed: " + str(weapon_item.Speed))
    print("Weapon Accuracy: " + str(weapon_item.Accuracy))
    print("Weapon Max Damage: " + str(weapon_item.Maxdmg))
    print("Weapon Min Damage: " + str(weapon_item.Mindmg))
    print("Weapon Crit Chance: " + str(weapon_item.critchance))
    print("Weapon Crit Damage: " + str(weapon_item.critdamage))
    print("Weapon Slot: " + weapon_item.slot)
    print("Weapon Condition: " + str(weapon_item.condition))
    print("Weapon Owner: " + weapon_item.owner)
    print("Weapon Special: " + weapon_item.special)
    print("Weapon Rating: " + str(weapon_item.rating))

def saveweapon(self):
    """Saves the weapon object to a database."""
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weapons (name, type, type2, AP, dmgtype, Speed, Accuracy,"
    "Maxdmg, Mindmg, critchance, critdamage, slot, condition, owner, special, rating)"
    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.name, self.type, self.type2, self.AP, self.dmgtype,
    self.Speed, self.Accuracy, self.Maxdmg, self.Mindmg, self.critchance, self.critdamage, self.slot,
    self.condition, self.owner, self.special, self.rating))
    conn.commit()
    conn.close()

for _ in range (50):
    weapon_item = generateweapon()
    printweapon(weapon_item)
    saveweapon(weapon_item)

