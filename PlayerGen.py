import random
import sqlite3
import json
import Database
from namegen import playernamegen
import WeaponGen
import ArmourGen
import string
def racegen():
    races = ["Human", "Elf", "Dwarf", "Orc", "Goblin", "Troll", "Cyborg", "Android", "Mutant", "Bipodal Alien",
             "Ogre", "Vampire", "Werewolf", "Zombie", "Ghost", "Demon", "Angel", "Dragon", "Phoenix" 
             "Tripodal Alien", "Mutated Insect", "Dragon","Being", "Miscreation", "Skeleton", "Human", "Beast",
             "Gargoyle", "Vampire", "Crocodile", "Phenomenon", "Lion", "Griffin", "Giant", "Ghoul", "Banshee",
             "Screamer", "Mutant", "Wraith", "Behemoth", "Spawn", "Spider", "Ape", "Robot", "Tiger", "Unicorn",
             "Kliknik", "Arachnid", "Nurling", "Demon", "Bug", "Scorpion", "Flyer", "Canine", "Reptile",
             "Cyclops", "Kraken", "Centaur", "Locust", "Penguin", "Mandrill", "Floranoid", "Weasel", "Hydrogue",
             "Faero", "Fairy", "Rancor", "Tusken", "Sardaukar", "Fremen", "Sandworm", "Witch"]
    return random.choice(races)

#def racialbonusgen(race,rb1,rb2):

def generateplayerarmour(slot, owner):
    # Placeholder function for generating player armour
    # In a real implementation, this would generate and return an armour object
    item_id = ArmourGen.armour(slot=slot, owner=owner)
    return item_id.lrid

def weapon(owner):
# Placeholder function for generating player weapon
    # In a real implementation, this would generate and return a weapon object
    item_id = WeaponGen.weapon(owner=owner)
    return item_id.lrid

def generateuid():
    """Generates a random string of letters and numbers with the specified length."""
    length=25
    characters = string.ascii_letters + string.digits  # Combine letters and digits
    return ''.join(random.choices(characters, k=length))

def ratingscore(head, shoulder, arm, hand, chest, pants, boots, mainhand):

    """Calculates the rating score based on the player's equipment."""
    #pull the item ratings from the database
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (head,))
    headrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (shoulder,))
    shoulderrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (arm,))
    armrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (hand,))
    handrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (chest,))
    chestrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (pants,))
    pantsrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM armour WHERE id = ?", (boots,))
    bootsrating = cursor.fetchone()
    cursor.execute("SELECT rating FROM weapons WHERE id = ?", (mainhand,))
    weaponrating = cursor.fetchone()
    #calculate the rating score
    #sum the ratings of all the items
    totalrating = (headrating[0] + shoulderrating[0] + armrating[0] + handrating[0] + chestrating[0] +
                   pantsrating[0] + bootsrating[0] + weaponrating[0])
    #calculate the average rating
    avgrating = int(totalrating / 8)
    return avgrating




class HumanPlayer:

    def __init__(self, type=None, uid=None, race=None, rb1=None, rb2=None, rb3=None, name=None, hp=None, head=None,
                 shoulder=None, arm=None, hand=None, chest=None, pants=None, boots=None, mainhand=None, offhand=None,
                 jwl1=None, jwl2=None, arminv=None, weaponinv=None, jwlinv=None, iteminv=None, lightranged=None,
                 medranged=None, heavyranged=None, launchers=None, unarmed=None, lightmelee=None, mediummelee=None,
                 heavymelee=None, armrep=None, weaponrep=None, rating=None):
        self.type = type if type is not None else "Human"
        self.uid = uid if uid is not None else generateuid()
        self.race = race if race is not None else racegen()
        self.rb1 = rb1 if rb1 is not None else 0
        self.rb2 = rb2 if rb2 is not None else 0
        self.rb3 = rb3 if rb3 is not None else 0
        self.name = name if name is not None else playernamegen(self.race)

        self.hp = hp if hp is not None else random.randint(1000, 50000)

        self.head = head if head is not None else generateplayerarmour("Head", self.uid)
        self.shoulder = shoulder if shoulder is not None else generateplayerarmour("Shoulder", self.uid)
        self.arm = arm if arm is not None else generateplayerarmour("Arm", self.uid)
        self.hand = hand if hand is not None else generateplayerarmour("Hand", self.uid)
        self.chest = chest if chest is not None else generateplayerarmour("Chest", self.uid)
        self.pants = pants if pants is not None else generateplayerarmour("Pants", self.uid)
        self.boots = boots if boots is not None else generateplayerarmour("Boots", self.uid)

        self.mainhand = mainhand if mainhand is not None else WeaponGen.weapon(owner=self.uid).lrid

        self.offhand = offhand if offhand is not None else 0
        self.jwl1 = jwl1 if jwl1 is not None else 0
        self.jwl2 = jwl2 if jwl2 is not None else 0
        self.arminv = arminv if arminv is not None else []
        self.weaponinv = weaponinv if weaponinv is not None else []
        self.jwlinv = jwlinv if jwlinv is not None else []
        self.iteminv = iteminv if iteminv is not None else []
        self.lightranged = lightranged if lightranged is not None else  {"xp":0,"level":0}
        self.medranged = medranged if medranged is not None else {"xp":0,"level":0}
        self.heavyranged = heavyranged if heavyranged is not None else {"xp":0,"level":0}
        self.launchers = launchers if launchers is not None else {"xp":0,"level":0}
        self.unarmed = unarmed if unarmed is not None else {"xp":0,"level":0}
        self.lightmelee = lightmelee if lightmelee is not None else {"xp":0,"level":0}
        self.mediummelee = mediummelee if mediummelee is not None else {"xp":0,"level":0}
        self.heavymelee = heavymelee if heavymelee is not None else {"xp":0,"level":0}
        self.armrep = armrep if armrep is not None else 0
        self.weaponrep = weaponrep if weaponrep is not None else 0
        self.rating = rating if rating is not None else ratingscore(self.head, self.shoulder, self.arm,
                                                                    self.hand, self.chest, self.pants, self.boots,
                                                                    self.mainhand)
        savep_to_db(self)


class cpuplayer:
    def __init__(self, type=None, uid=None, race=None, rb1=None, rb2=None, rb3=None, name=None, hp=None, head=None,
                 shoulder=None, arm=None, hand=None, chest=None, pants=None, boots=None, mainhand=None, offhand=None,
                 jwl1=None, jwl2=None, lightranged=None, medranged=None, heavyranged=None, launchers=None,
                 unarmed=None, lightmelee=None, mediummelee=None, heavymelee=None, rating=None):
        self.type = type if type is not None else "CPU"
        self.uid = uid if uid is not None else generateuid()
        self.race = race if race is not None else racegen()
        self.rb1 = rb1 if rb1 is not None else 0
        self.rb2 = rb2 if rb2 is not None else 0
        self.rb3 = rb3 if rb3 is not None else 0
        self.name = name if name is not None else playernamegen(self.race)
        self.hp = hp if hp is not None else random.randint(1000, 50000)

        self.head = head if head is not None else generateplayerarmour("Head", self.uid)
        self.shoulder = shoulder if shoulder is not None else generateplayerarmour("Shoulder", self.uid)
        self.arm = arm if arm is not None else generateplayerarmour("Arm", self.uid)
        self.hand = hand if hand is not None else generateplayerarmour("Hand", self.uid)
        self.chest = chest if chest is not None else generateplayerarmour("Chest", self.uid)
        self.pants = pants if pants is not None else generateplayerarmour("Pants", self.uid)
        self.boots = boots if boots is not None else generateplayerarmour("Boots", self.uid)

        self.mainhand = mainhand if mainhand is not None else WeaponGen.weapon(owner=self.uid).lrid

        self.offhand = offhand if offhand is not None else 0
        self.jwl1 = jwl1 if jwl1 is not None else 0
        self.jwl2 = jwl2 if jwl2 is not None else 0
        self.lightranged = lightranged if lightranged is not None else {"xp":0,"level":random.randint(1, 10)}
        self.medranged = medranged if medranged is not None else {"xp":0,"level":random.randint(1, 10)}
        self.heavyranged = heavyranged if heavyranged is not None else {"xp":0,"level":random.randint(1, 10)}
        self.launchers = launchers if launchers is not None else {"xp":0,"level":random.randint(1, 10)}
        self.unarmed = unarmed if unarmed is not None else {"xp":0,"level":random.randint(1, 10)}
        self.lightmelee = lightmelee if lightmelee is not None else {"xp":0,"level":random.randint(1, 10)}
        self.mediummelee = mediummelee if mediummelee is not None else {"xp":0,"level":random.randint(1, 10)}
        self.heavymelee = heavymelee if heavymelee is not None else {"xp":0,"level":random.randint(1, 10)}
        self.rating = rating if rating is not None else ratingscore(self.head, self.shoulder, self.arm,
                                                                    self.hand, self.chest, self.pants, self.boots,
                                                                    self.mainhand)
        savecpu_to_db(self)

def savep_to_db(self):
    #save the player to the player table in the game.db database

    #convert dictionaries to json strings
    jlightranged = json.dumps(self.lightranged)
    jmedranged = json.dumps(self.medranged)
    jheavyranged = json.dumps(self.heavyranged)
    jlaunchers = json.dumps(self.launchers)
    junarmed = json.dumps(self.unarmed)
    jlightmelee = json.dumps(self.lightmelee)
    jmediummelee = json.dumps(self.mediummelee)
    jheavymelee = json.dumps(self.heavymelee)
    jarminv = json.dumps(self.arminv)
    jweaponinv = json.dumps(self.weaponinv)
    jjwlinv = json.dumps(self.jwlinv)
    jiteminv = json.dumps(self.iteminv)


    #connect to the database
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO players (type, uid, race, rb1, rb2, rb3, name, hp, head, shoulder, arm, hand, "
                   "chest, pants, boots, mainhand, offHand, jwl1, jwl2, arminv, weaponinv, jwlinv, iteminv, "
                   "lightranged, medranged, heavyranged, launchers, unarmed, lightmelee, mediummelee, heavymelee, "
                   "armrep, weaponrep, rating) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (self.type, self.uid, self.race, self.rb1, self.rb2, self.rb3, self.name, self.hp,
                     self.head, self.shoulder, self.arm, self.hand, self.chest, self.pants, self.boots,
                        self.mainhand, self.offhand, self.jwl1, self.jwl2, jarminv, jweaponinv,
                        jjwlinv, jiteminv, jlightranged, jmedranged, jheavyranged, jlaunchers,
                        junarmed, jlightmelee, jmediummelee, jheavymelee, self.armrep, self.weaponrep,
                        self.rating))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

def savecpu_to_db(self):
    #convert dictionaries to json strings
    jlightranged = json.dumps(self.lightranged)
    jmedranged = json.dumps(self.medranged)
    jheavyranged = json.dumps(self.heavyranged)
    jlaunchers = json.dumps(self.launchers)
    junarmed = json.dumps(self.unarmed)
    jlightmelee = json.dumps(self.lightmelee)
    jmediummelee = json.dumps(self.mediummelee)
    jheavymelee = json.dumps(self.heavymelee)



    #connect to the database
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO players (type, uid, race, rb1, rb2, rb3, name, hp, head, shoulder, arm, hand, "
                   "chest, pants, boots, mainhand, offHand, jwl1, jwl2,"
                   "lightranged, medranged, heavyranged, launchers, unarmed, lightmelee, mediummelee, heavymelee, "
                   "rating) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (self.type, self.uid, self.race, self.rb1, self.rb2, self.rb3, self.name, self.hp,
                    self.head, self.shoulder, self.arm, self.hand, self.chest, self.pants, self.boots,
                    self.mainhand, self.offhand, self.jwl1, self.jwl2, jlightranged, jmedranged, jheavyranged,
                    jlaunchers, junarmed, jlightmelee, jmediummelee, jheavymelee,
                    self.rating))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection


    #insert the player into the database
cpuplayer()
HumanPlayer()



