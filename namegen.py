import random

def generateAname(type, slot, setbonus, rating, specproc):
    """
    Generates a name for an armour item based on its type and slot.
    """
    # Define possible prefixes and suffixes for the armour item name
    sufffixes = ["Ancients", "Mystics", "Cursed", "Enchanted", "Divine", "Fabled", "Arcane", "Ethereal", "Spectral",
                 "Phantom Lord", "Wraith King", "Void Dweller", "Titan", "Dragonkin", "Elementals", "Arcane",
                 "Runic", "Shadow", "Lightbringer", "Darkbane", "Stormforged", "Frostforge", "Flameforge",
                 "Earthshatter", "Thunderstriker", "Bloodbound", "Soulbound", "Spiritbound", "Nightfall",
                 "Dawnbringer", "Twilight", "Starforged", "Sunfire", "Moonshadow", "Voidwalker", "Stormcaller",
                 "Firewalker", "Icebreaker", "Earthwarden"]
    #suffixes = ["of Power", "of Agility", "of Strength", "of Wisdom", "of Resilience", "of Fortitude", "of Endurance", "of Protection", "of the Guardian", "of the Sentinel", "of the Protector", "of the Defender", "of the Champion", "of the Conqueror", "of the Vanquisher", "of the Slayer", "of the Hunter", "of the Beastmaster", "of the Warlord", "of the Berserker", "of the Gladiator", "of the Duelist", "of the Assassin", "of the Rogue", "of the Trickster", "of the Shadow", "of the Nightblade", "of the Phantom", "of the Specter"
               #     "of the Wraith", "of the Revenant", "of the Lich", "of the Necromancer", "of the Warlock", "of the Sorcerer", "of the Wizard", "of the Mage", "of the Alchemist", "of the Enchanter", "of the Illusionist", "of the Elementalist", "of the Pyromancer", "of the Cryomancer", "of the Geomancer", "of the Aeromancer", "of the Hydromancer", "of the Chronomancer", "of the Necromancer", "of the Summoner"]

    setbonusn = ["Orion the Hunter", "The Beastmaster", "The Berserker", "The Gladiator", "The Duelist", "The Assassin",
                "The Rogue", "The Trickster", "The Shadow", "The Nightblade", "The Phantom", "The Specter", "The Wraith",
                "The Revenant", "The Lich", "The Necromancer", "The Warlock", "The Sorcerer", "The Wizard", "The Mage",
                "The Alchemist", "The Enchanter", "The Illusionist", "The Elementalist", "The Pyromancer", "The Cryomancer",
                "The Geomancer", "The Aeromancer", "The Hydromancer"]

    if specproc == None:
        specprocn = 0
    elif sum(1 for proc in specproc) == 2:
        specprocn = str(random.choice(specproc))
    elif sum(1 for proc in specproc) == 3:
        specprocn = str(random.choice(specproc))
    else:
        specprocn = str(random.choice(specproc))   # Choose a random special proc from the list

    if type == "Heavy":
        Material = ["Steel", "Titanium", "Adamantium", "Obsidian", "Starforged", "Nanocarbon", "Plasteel", "Tungsten",
                    "Dragonforged", "Titanium Alloy"]
    elif type == "Medium":
        Material = ["Composite", "Carbon" "Plate", "Composite", "Plate", "Iron", "Brigandine", "Dragonhide",
                    "Studded Leather", "Exotic Alloy", "Ceramic Composite"]
    elif type == "Light":
        Material = ["Leather", "Bone", "Hide", "Fur", "Scale", "Chainmail", "Scale Mail", "Bronze Plated", "Graphene",
                    "Lightweight Composite"]
    elif type == "Cloth":
        Material = ["Cotton", "Linen", "Wool", "Silk", "Velvet", "Satin", "Brocade", "Kevlar", "Micro-fibre"]

    if slot == "Head":
        slotname = random.choice(["Helm", "Crown", "Cap", "Mask"])
    elif slot == "Shoulder":
        slotname = random.choice(["Pauldrons", " Spaulders", "Shoulder Guards", "Shoulder Pads", "Shoulder Plates",
                                  "Shoulder Armor", "Shoulder Capes", "Shoulder Cloaks"])
    elif slot == "Arm":
        slotname = random.choice(["Bracers", "Arm Guards", "Bicep Guards", "Sleeves", "Vambraces", "Cuffs", "Armlets"])
    elif slot == "Hand":
        slotname = random.choice(["Gloves", "Gauntlets", "Mittens"])
    elif slot == "Chest":
        slotname = random.choice(["Chestplate", "Cuirass", "Hauberk"])
    elif slot == "Pants":
        slotname = random.choice(["Leggings", "Pants", "Trousers"])
    elif slot == "Boots":
        slotname = random.choice(["Boots", "Shoes", "Sandals"])

    if rating > 90:
        ratingname = "Ascended"
    elif rating > 85:
        ratingname = "Celestial"
    elif rating > 80:
        ratingname = "Exalted"
    elif rating > 75:
        ratingname = "Mythic"
    elif rating > 70:
        ratingname = "Legendary"
    elif rating > 65:
        ratingname = "Epic"
    elif rating > 60:
        ratingname = "Superior"
    elif rating > 55:
        ratingname = "Ornate"
    elif rating > 50:
        ratingname = "Distinguished"
    elif rating > 45:
        ratingname = "Sturdy"
    elif rating > 40:
        ratingname = "Notable"
    elif rating > 35:
        ratingname = "Uncommon"
    else:
        ratingname = "Common"

    # Choose a random prefix and suffix
    #prefix = random.choice(prefixes)
    #suffix = random.choice(suffixes)

    protfillerlist = ("protection", "resistance", "defense", "toughness", "fortification",
                      "shielding", "guardianship", "safeguarding", "deflection", "absorption")
    protectfiller = random.choice(protfillerlist)
    # Combine them with the type and slot to create the item name
    materialname = random.choice(Material)

    if rating > 60:
        if setbonus == None:
            if specprocn == 0:
                returnname = (f"{ratingname} {materialname} {slotname}") #no set bonus or special proc
            else:
                str(specprocn)
                returnname = (f"{ratingname} {materialname} {slotname} of {specprocn} {protectfiller}") #special proc but no set bonus
        else:
                returnname = (f"{ratingname} {materialname} {slotname} of {setbonus}") #set bonus but no special proc

    else:
        if setbonus == None:
            returnname = (f"{ratingname} {materialname} {slotname}")
        else:
            returnname = (f"{ratingname} {materialname} {slotname} of {setbonus}") #set bonus but no special proc

    return returnname


def generateWname(type2, AP, rating, slot):

    if type2 == "Launcher":
        type2n = str(random.choice(["Rocket Launcher", "Missile Launcher", "Grenade Launcher", "Flame Thrower", "Plasma Emitter",
                     "Energy Cannon", "Pulse Blaster", "Shockwave Emitter"]))
    elif type2 == "Rifle":
        type2n = str(random.choice(["Assault Rifle", "Sniper Rifle", "Battle Rifle",  "Marksman Rifle"]))
    elif type2 == "Pistol":
        type2n = str(random.choice(["Revolver", "Semi-Automatic Pistol", "Automatic Pistol", "Submachine Gun", "Blaster"]))
    elif type2 == "Carbine":
        type2n = str(random.choice(["Carbine", "Compact Carbine", "Submachine Carbine", "Assault Carbine", "Battle Carbine"]))
    elif type2 == "Longbow":
        type2n = str(random.choice(["Longbow", "Compound Bow", "Recurve Bow"]))
    elif type2 == "Crossbow":
        type2n = str(random.choice(["Crossbow", "Repeating Crossbow", "HandCrossbow"]))
    elif type2 == "Bow":
        type2n = str(random.choice(["Bow", "Shortbow", "Composite Bow"]))
    elif type2 == "Dagger":
        type2n = str(random.choice(["Dagger", "Knife", "Dirk", "Kris"]))
    elif type2 == "Blade":
        type2n = str(random.choice(["Blade", "Shank", "Sabre", "Scimitar"]))
    elif type2 == "Sword":
        type2n = str(random.choice(["Sword", "Broadsword", "Curved Sword", "Rapier"]))
    elif type2 == "Duster":
        type2n = str(random.choice(["Knuckle Duster" "Brass Knuckles", "Knuckle Blade"]))
    elif type2 == "Fist":
        type2n = str(random.choice(["Fist", "Punching Dagger", "Fist Blade"]))
    elif type2 == "Knuckler":
        type2n = str(random.choice(["Knuckler", "Vibro Knuckler", "Power Fist"]))
    elif type2 == "Polearm":
        type2n = str(random.choice(["Polearm", "Halberd", "Glaive"]))
    elif type2 == "Lance":
        type2n = str(random.choice(["Lance", "Javelin", "Pike"]))
    elif type2 == "Spear":
        type2n = str(random.choice(["Spear", "Trident", "Harpoon"]))
    elif type2 == "Warhammer":
        type2n = str(random.choice(["Warhammer", "Maul", "War Club"]))
    elif type2 == "Axe":
        type2n = str(random.choice(["Axe", "Battle Axe", "Hatchet", "Tomahawk"]))
    elif type2 == "Greatsword":
        type2n = str(random.choice(["Greatsword", "Claymore", "Zweihander"]))

    if rating > 90:
        ratingname = "Ascended"
    elif rating > 85:
        ratingname = "Celestial"
    elif rating > 80:
        ratingname = "Exalted"
    elif rating > 75:
        ratingname = "Mythic"
    elif rating > 70:
        ratingname = "Legendary"
    elif rating > 65:
        ratingname = "Epic"
    elif rating > 60:
        ratingname = "Superior"
    elif rating > 55:
        ratingname = "Ornate"
    elif rating > 50:
        ratingname = "Distinguished"
    elif rating > 45:
        ratingname = "Sturdy"
    elif rating > 40:
        ratingname = "Notable"
    elif rating > 35:
        ratingname = "Uncommon"
    else:
        ratingname = "Common"

    suffixes = ["of Power", "of Agility", "of Strength", "of Wisdom", "of Resilience", "of Fortitude", "of Endurance",
                "of Protection", "of the Guardian", "of the Sentinel", "of the Protector", "of the Defender",
                "of the Champion", "of the Conqueror", "of the Vanquisher", "of the Slayer", "of the Hunter",
                "of the Beastmaster", "of the Warlord", "of the Berserker", "of the Gladiator", "of the Duelist",
                "of the Assassin", "of the Rogue", "of the Trickster", "of the Shadow", "of the Nightblade",
                "of the Phantom", "of the Specter", "of the Wraith", "of the Revenant", "of the Lich",
                "of the Necromancer", "of the Warlock", "of the Sorcerer", "of the Wizard", "of the Mage"]

    randomsuffix = str(random.choice(suffixes)) # Choose a random suffix from the list

    weaponname = str(f"{ratingname} {type2n} {randomsuffix}") #name of weapon with AP

    return weaponname
