import random

def generateAname(type, slot, setbonus, rating, specproc):
    """
    Generates a name for an armour item based on its type and slot.
    """
    # Define possible prefixes and suffixes for the armour item name
    sufffixes = ["Ancient", "Mystic", "Cursed", "Enchanted", "Divine", "Fabled", "Legendary", "Epic", "Rare", "Common", "Uncommon", "Mythic", "Heroic", "Arcane", "Celestial", "Infernal", "Ethereal", "Spectral", "Phantom", "Wraith", "Void", "Titanic", "Dragonkin", "Demonic", "Celestial", "Elemental", "Arcane", "Runic", "Shadow", "Lightbringer", "Darkbane", "Stormforged",
                    "Frostforged", "Flameforged", "Earthshatter", "Thunderstrike", "Bloodbound", "Soulbound", "Spiritbound", "Nightfall", "Dawnbringer", "Twilight", "Starforged", "Sunfire", "Moonshadow", "Voidwalker", "Stormcaller", "Firewalker", "Icebreaker", "Earthwarden"]
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
        specprocn = str(specproc)  # Choose a random special proc from the list

    if type == "Heavy":
        Material = ["Steel", "Iron", "Bronze", "Titanium", "Adamantium", "Obsidian"]
    elif type == "Medium":
        Material = ["Composite", "Plate", "Composite", "Plate", "Scale Mail", "Brigandine", "Dragonhide", "Lamellar", "Cuirass", "Hauberk", "Studded Leather"]
    elif type == "Light":
        Material = ["Leather", "Bone", "Hide", "Fur", "Scale", "Chainmail"]
    elif type == "Cloth":
        Material = ["Cotton", "Linen", "Wool", "Silk", "Velvet", "Satin", "Brocade"]

    if slot == "Head":
        slotname = random.choice(["Helm", "Crown", "Cap", "Mask"])
    elif slot == "Shoulder":
        slotname = random.choice(["Pauldrons", " Spaulders", "Shoulder Guards", "Shoulder Pads", "Shoulder Plates", "Shoulder Armor", "Shoulder Capes", "Shoulder Cloaks"])
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

    if setbonus == None:
        if specprocn == 0:
            returnname = (f"{ratingname} {materialname} {slotname}") #no set bonus or special proc
        else:
            returnname = (f"{ratingname} {materialname} {slotname} of {specprocn} {protectfiller}") #special proc but no set bonus
    else:
        if specprocn == 0:
            returnname = (f"{ratingname} {materialname} {slotname} of {setbonusn}") #set bonus but no special proc
        else:
            returnname = (f"{ratingname} {materialname} {slotname} of {setbonusn} and {specprocn} {protectfiller}") #set bonus and special proc

    return returnname
