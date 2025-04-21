import random
import namegen
import json
import sqlite3
from namegen import generateAname
from Database import Database

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
def genarmourtype():
    """
    Generates a random armour type.
    """
    lixy = random.randint(0, 100)

    if lixy > 95:
        return "Heavy"
    elif lixy > 80:
        return "Medium"
    elif lixy > 50:
        return "Light"
    else:
        return "Cloth"



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
    special_procs = ["Kinetic", "Heat", "Energy", "Projectile", "Electric", "Cold", "Acid", "Explosive", "Exotic",
                     "Dark", "Sonic", "Water", "Divine"]
    #choose 1, 2 or 3 special procs based on a weighting system
    spng = random.randint(0, 100)
    if spng < 5: # 5% chance of getting no special
        result = None
    elif spng < 45: # 40% chance of getting one special
        result = [random.choice(special_procs)]
    elif spng < 90: # 45% chance of getting two specials
        result = random.sample(special_procs, 2)
    else: # 10% chance of getting three specials
        result = random.sample(special_procs, 3)

    return result

def modifiergen(provrating):
    """
    Generates a random modifier for the armour item.
    """
    # Define possible modifiers
    modifiers = ["Critical Hit Chance", "Critical Hit Damage", "Two Handed Melee Speed", "One Handed Melee Speed", "Unarmed Melee Speed",
                 "Pistol Attack Speed", "Carbine Attack Speed","Rifle Attack Speed", "Heavy Weapon Speed", "Melee Defence", "Ranged Toughness"]
    ded = random.randint(0, 100)
    if provrating > 80 and ded > 20:
        return random.choice(modifiers)
    elif provrating > 70 and ded > 35:
        return random.choice(modifiers)
    elif ded > 80:
        return random.choice(modifiers)
    else:
        return None

def modifiergen2(provrating):
    """
    Generates a random modifier for the armour item.
    """
    # Define possible modifiers
    modifiers = ["Critical Hit Chance", "Critical Hit Accuracy", "Two Handed Melee Accuracy", "One Handed Melee Accuracy", "Unarmed Melee Accuracy",
                 "Pistol Attack Accuracy", "Carbine Attack Accuracy","Rifle Attack Accuracy", "Heavy Weapon Accuracy", "Ranged Defence", "Melee Toughness"]
    ded = random.randint(0, 100)
    if provrating > 80 and ded > 35:
        return random.choice(modifiers)
    elif provrating > 70 and ded > 65:
        return random.choice(modifiers)
    elif ded > 95:
        return random.choice(modifiers)
    else:
        return None

def modifiervalgen(modifier, provrating):

    if modifier == None:
        return None
    else:
        if provrating > 78:
            return random.randint(19, 25)
        elif provrating > 68:
            return random.randint(17, 23)
        elif provrating > 58:
            return random.randint(15, 21)
        else:
            return random.randint(1, 17)

def vulngen(specproc):
    """
    Generates a random number of vulnerability for the armour item 0-3:
    """
    vulnist = ["Kinetic", "Heat", "Energy", "Projectile", "Electric", "Cold", "Acid", "Explosive", "Exotic", "Dark",
               "Sonic", "Water", "Devine"]
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

def setbonuscalc(provrating):
    """
    Generates a set bonus for the armour item.
    """
    sbng = random.randint(0, 100)
    #check whether a setbonus should be applied
    if provrating > 79 and sbng > 20:
        return random.choice(setbonus)
    elif provrating > 69 and sbng > 35:
        return random.choice(setbonus)
    elif provrating > 59 and sbng > 75:
        return random.choice(setbonus)
    elif sbng > 96:
        return random.choice(setbonus)
    else:
        return None

def save_to_db(self):
    """
    Saves the generated armour item to the SQLite database.
    """
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    owner = "player1"
    # Insert the armour item data

    #serialize lists to json strings
    specproc_json = json.dumps(self.specproc) if self.specproc is not None else None
    vuln_json = json.dumps(self.vuln) if self.vuln is not None else None
    baseproc_json = json.dumps(self.baseproc) if self.baseproc is not None else None

    cursor.execute("INSERT INTO armour (name, slot, type, typeval, specproc, specres, baseproc, baseres, vuln, "
              "condition, socket, modifiers1, modifiers2, modifiers1v, modifiers2v, setbonus, rating, owner)"
             "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (self.name, self.slot, self.type, self.typeval, specproc_json, self.specres, baseproc_json, self.baseres, vuln_json,
                    self.condition, self.socket, self.modifiers1, self.modifiers2, self.modifiers1v, self.modifiers2v, self.setbonus,
                    self.rating,owner))
    # Commit the changes and close the connection
    conn.commit()
    conn.close()



class armour:
    """
    Represents an armour item with various attributes.
    """
    def __init__(self, name=None, slot=None, type=None, typeval=None, specproc=None, specres=None, baseproc=None, baseres=None, vuln=None, condition=None, socket=None, modifiers1=None, modifiers2=None, modifiers1v=None, modifiers2v=None, setbonus=None, rating=None):

        self.type = type if type is not None else genarmourtype()
        self.typeval = armourtypes[self.type]
        self.slot = slot if slot is not None else random.choice(slots)
        self.specproc = specproc if specproc is not None else specprocgen()
        self.specres = specres if specres is not None else random.randint(76, 95)
        self.vuln = vuln if vuln is not None else vulngen(self.specproc)
        self.baseproc = baseproc if baseproc is not None else basegen(self.specproc, self.vuln)
        self.baseres = baseres if baseres is not None else random.randint(45, 75)
        specproc_count = len(self.specproc) if self.specproc is not None else 0
        basecount = len(self.baseproc) if self.baseproc is not None else 0

        provrating = int(
            (((((self.specres - 75) + (self.baseres - 45)) / 50) * 2) +
            (specproc_count / 3) +
            ((basecount + specproc_count) / 13)) / 4 * 100)


        # Calculate the condition based on the provided rating
        if condition is None:
            if provrating > 70:
                self.condition = random.randint(85000, 120000)
            elif provrating > 60:
                self.condition = random.randint(60000, 95000)
            elif provrating > 50:
                self.condition = random.randint(50000, 85000)
            else:
                self.condition = random.randint(10000, 75000)
        else:
            self.condition = condition

        # Calculate the socket based on the provided rating
        if socket is None:
            if provrating > 65:
                self.socket = random.randint(1, 2)
            else:
                self.socket = random.randint(0, 1)
        else:
            self.socket = socket

        self.modifiers1 = modifiers1 if modifiers1 is not None else modifiergen(provrating)
        self.modifiers2 = modifiers2 if modifiers2 is not None else modifiergen2(provrating)
        self.modifiers1v = modifiers1v if modifiers1v is not None else modifiervalgen(self.modifiers1, provrating)
        self.modifiers2v = modifiers2v if modifiers2v is not None else modifiervalgen(self.modifiers2, provrating)
        self.setbonus = setbonus if setbonus is not None else setbonuscalc(provrating)

        #for rating calculation
        modifiers1_count = 1 if self.modifiers1 is not None else 0
        modifiers2_count = 1 if self.modifiers2 is not None else 0
        setbonus_count = 1 if self.setbonus is not None else 0
        modifiers1v_count = self.modifiers1v if self.modifiers1v is not None else 0
        modifiers2v_count = self.modifiers2v if self.modifiers2v is not None else 0


        self.rating = int((
                                  (self.condition / 120000) +
                                  (((((self.specres - 75) / 20) * specproc_count)) * 3)+
                                  (((((self.baseres - 45) / 30) * basecount)) * 3) +
                                  (self.socket / 2) +
                                  ((modifiers1_count / 1)) +
                                  ((modifiers2_count / 1)) +
                                  ((modifiers1v_count / 25)) +
                                  ((modifiers2v_count / 25)) +
                                  ((setbonus_count / 1) * 3)) / ((9 + (specproc_count * 3) + (basecount * 3))) * 100)

        self.name = name if name is not None else generateAname(self.type,self.slot,self.setbonus,self.rating,self.specproc)

        save_to_db(self)



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
    print(f"Type Value: {armour_item.typeval}")
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


for _ in range(50):
    print_armour(generate_armour()) #generate and print a random armour item

#write the generated armour item to a json file and store in the database






