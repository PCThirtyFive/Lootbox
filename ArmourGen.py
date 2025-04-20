import random
import namegen
import json
import sqlite3
from namegen import generateAname

slots = ["Head", "Shoulder", "Arm", "Hand", "Chest", "Pants", "Boots"]
armourtypes = {"Heavy" :4,
               "Medium":3,
               "Light":2,
               "Cloth":1}

setbonus = ["Orion the Hunter", "The Beastmaster", "The Berserker", "The Gladiator", "The Duelist", "The Assassin",
            "The Rogue", "The Trickster", "The Shadow", "The Nightblade", "The Phantom", "The Specter", "The Wraith",
            "The Revenant", "The Lich", "The Necromancer", "The Warlock", "The Sorcerer", "The Wizard", "The Mage",
            "The Alchemist", "The Enchanter", "The Illusionist", "The Elementalist", "The Pyromancer", "The Cryomancer",
            "The Geomancer", "The Aeromancer", "The Hydromancer"]


def setbonuscalc():
    """
    Generates a set bonus for the armour item.
    """
    #check whether a setbonus should be applied
    if random.randint(0, 10) == 5:
        # Choose a random set bonus from the list
        return random.choice(setbonus)
    else:
        return None

def specprocgen():
    """
    Generates a special proc for the armour item.
    """
    # Define possible special procs
    special_procs = ["Kinetic", "Heat","Energy", "Projectile", "Electric","Cold","Acid","Explosive","Exotic","Dark","Sonic","Water","Devine"]
    #choose 1, 2 or 3 special procs based on a weighting system
    spng = random.randint(0, 100)
    if spng < 5: # 5% chance of getting no special
        return None
    elif spng < 45: # 40% chance of getting one special
        return random.choice(special_procs)
    elif spng < 90: # 45% chance of getting two specials
        return random.sample(special_procs, 2)
    else: # 10% chance of getting three specials
        return random.sample(special_procs, 3)

def modifiergen():
    """
    Generates a random modifier for the armour item.
    """
    # Define possible modifiers
    modifiers = ["Critical Hit Chance", "Critical Hit Damage", "Two Handed Melee Speed", "One Handed Melee Speed", "Unarmed Melee Speed",
                 "Pistol Attack Speed", "Carbine Attack Speed","Rifle Attack Speed", "Heavy Weapon Speed", "Melee Defence", "Ranged Toughness"]
    ded = random.randint(0, 100)
    if ded > 96:
        return random.choice(modifiers)
    else:
        return None

def modifiergen2():
    """
    Generates a random modifier for the armour item.
    """
    # Define possible modifiers
    modifiers = ["Critical Hit Chance", "Critical Hit Accuracy", "Two Handed Melee Accuracy", "One Handed Melee Accuracy", "Unarmed Melee Accuracy",
                 "Pistol Attack Accuracy", "Carbine Attack Accuracy","Rifle Attack Accuracy", "Heavy Weapon Accuracy", "Ranged Defence", "Melee Toughness"]
    ded = random.randint(0, 100)
    if ded > 96:
        return random.choice(modifiers)
    else:
        return None

def modifiervalgen(modifier):

    if modifier == None:
        return None
    else:
        return random.randint(1, 25)

def vulngen(specproc):
    """
    Generates a random number of vulnerability for the armour item 0-3:
    """
    vulnist = ["Kinetic", "Heat","Energy", "Projectile", "Electric","Cold","Acid","Explosive","Exotic","Dark","Sonic","Water","Devine"]
    specproc1 = specproc
    # Remove the special proc from the list of possible vulnerabilities
    if specproc1 is not None:
        if isinstance(specproc1, list):
            for proc in specproc1:
                vulnist.remove(proc)
        else:
            vulnist.remove(specproc1)
    vlng = random.randint(0, 100)
    if vlng < 5: # 5% chance of getting no vulnerability
        return None
    elif vlng < 55: # 40% chance of getting one vulnerability
        return random.choice(vulnist)
    else: # 45% chance of getting two vulnerabilities
        return random.sample(vulnist, 2)

def basegen(specproc, vuln):
    """
    Generates a base resistance for the armour item.
    """
    # Define possible base resistances
    base_resistances = ["Kinetic", "Heat","Energy", "Projectile", "Electric","Cold","Acid","Explosive","Exotic","Dark","Sonic","Water","Devine"]
    # Remove the special proc and vulnerability from the list of possible resistances
    if specproc is not None:
        if isinstance(specproc, list):
            for proc in specproc:
                base_resistances.remove(proc)
        else:
            base_resistances.remove(specproc)
    if vuln is not None:
        if isinstance(vuln, list):
            for proc in vuln:
                base_resistances.remove(proc)
        else:
            base_resistances.remove(vuln)
    # Choose a random base resistance from the list
    return base_resistances

def setbonuscalc():
    """
    Generates a set bonus for the armour item.
    """
    #check whether a setbonus should be applied
    if random.randint(0, 10) == 5:
    # Choose a random set bonus from the list
        return random.choice(setbonus)
    else:
        return None

class armour:
    """
    Represents an armour item with various attributes.
    """
    def __init__(self, name, slot, type, typeval, specproc, specres, baseproc, baseres, vuln, condition, socket, modifiers1, modifiers2, modifiers1v, modifiers2v, setbonus, rating):
        self.condition = random.randint(10000, 95000)
        self.type = random.choice(list(armourtypes.keys()))
        self.typeval = armourtypes[self.type]
        self.slot = random.choice(slots)
        self.specproc = specprocgen()
        self.specres = random.randint(76, 95)
        self.vuln = vulngen(self.specproc)
        self.baseproc = basegen(self.specproc, self.vuln)
        self.baseres = random.randint(20, 75)
        self.socket = random.randint(0, 2)
        self.modifiers1 = modifiergen()
        self.modifiers2 = modifiergen2()
        self.modifiers1v = modifiervalgen(self.modifiers1)
        self.modifiers2v = modifiervalgen(self.modifiers2)
        self.setbonus = setbonuscalc()

        #for rating calculation
        if self.modifiers1 is None:
            modifiers1_count = 0
        else:
            modifiers1_count = 1
        if self.modifiers2 is None:
            modifiers2_count = 0
        else:
            modifiers2_count = 1
        if self.setbonus is None:
            setbonus_count = 0
        else:
            setbonus_count = 1
        if self.modifiers1v is None:
            modifiers1v_count = 0
        else:
            modifiers1v_count = self.modifiers1v
        if self.modifiers2v is None:
            modifiers2v_count = 0
        else:
            modifiers2v_count = self.modifiers2v

        self.rating = int(
            ((self.condition / 95000) +
            (self.typeval / 4) +
            (len(self.specproc) / 3) +  # Count the number of special procs
            (self.specres / 95) +
            (self.baseres / 75) +
            (self.socket / 2) +
            ((modifiers1_count /2 + 0)) +
            ((modifiers2_count / 2) + 0) +
            ((modifiers1v_count / 25) + 0) +
            ((modifiers2v_count / 25) + 0) +
            ((setbonus_count / 1) + 0)) / 11 * 100)

        self.name = generateAname(self.type,self.slot,self.setbonus,self.rating,self.specproc)

def generate_armour():
    """
    Generates a random armour item.
    """
    # Generate a random armour item
    return armour(None, None, None, None, None, None, None,
                  None, None, None, None, None, None, None,
                  None, None, None)
def print_armour(armour_item):
    print(f"Name: {armour_item.name}")
    print(f"Slot: {armour_item.slot}")
    print(f"Type: {armour_item.type}")
    print(f"Condition: {armour_item.condition}")
    print(f"Special Proc: {armour_item.specproc}")
    print(f"Special Resistance: {armour_item.specres}")
    print(f"Vulnerability: {armour_item.vuln}")
    print(f"Base Proc: {armour_item.baseproc}")
    print(f"Base Resistance: {armour_item.baseres}")
    print(f"Socket: {armour_item.socket}")
    print(f"Modifiers 1: {armour_item.modifiers1} ({armour_item.modifiers1v})")
    print(f"Modifiers 2: {armour_item.modifiers2} ({armour_item.modifiers2v})")
    print(f"Set Bonus: {armour_item.setbonus}")
    print(f"Rating: {armour_item.rating}")


for _ in range(100):
    print_armour(generate_armour()) #generate and print a random armour item
