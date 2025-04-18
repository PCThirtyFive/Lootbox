import random
import generateAname()
slots = ["Head", "Shoulder", "Arm", "Hand", "Chest", "Pants", "Boots"]
armourtypes = {"Heavy" :4,
               "Medium":3,
               "Light":2,
               "Cloth":1}




class armour:
    def __init__(self, name, slot, type, typeval, specproc, specres, baseproc, baseres, vuln, condtion, socket, modifiers,setbonus):
        self.condtion = random.randint(10000, 95000)
        self.type = random.choice(list(armourtypes.keys()))
        self.typeval = armourtypes[self.type]
        self.slot = random.choice(slots)
        self.name = generateAname(type,slot)
        self.specproc = specproc
        self.specres = specres
        self.baseproc = baseproc
        self.baseres = random.randint(20, 75)
        self.vuln = vuln
        self.socket = random.randint(0, 2)
        self.modifiers = modifiers
        self.setbonus = setbonus

