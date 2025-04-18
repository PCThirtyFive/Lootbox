import random

def generateAname(type, slot):
    """
    Generates a name for an armour item based on its type and slot.
    """
    # Define possible prefixes and suffixes for the armour item name
    prefixes = ["Ancient", "Mystic", "Cursed", "Enchanted", "Divine", "Fabled", "Legendary", "Epic", "Rare", "Common", "Uncommon", "Mythic", "Heroic", "Arcane", "Celestial", "Infernal", "Ethereal", "Spectral", "Phantom", "Wraith", "Void", "Titanic", "Dragonkin", "Demonic", "Celestial", "Elemental", "Arcane", "Runic", "Shadow", "Lightbringer", "Darkbane", "Stormforged",
                    "Frostforged", "Flameforged", "Earthshatter", "Thunderstrike", "Bloodbound", "Soulbound", "Spiritbound", "Nightfall", "Dawnbringer", "Twilight", "Starforged", "Sunfire", "Moonshadow", "Voidwalker", "Stormcaller", "Firewalker", "Icebreaker", "Earthwarden"]
    suffixes = ["of Power", "of Agility", "of Strength", "of Wisdom", "of Resilience", "of Fortitude", "of Endurance", "of Protection", "of the Guardian", "of the Sentinel", "of the Protector", "of the Defender", "of the Champion", "of the Conqueror", "of the Vanquisher", "of the Slayer", "of the Hunter", "of the Beastmaster", "of the Warlord", "of the Berserker", "of the Gladiator", "of the Duelist", "of the Assassin", "of the Rogue", "of the Trickster", "of the Shadow", "of the Nightblade", "of the Phantom", "of the Specter"
                    "of the Wraith", "of the Revenant", "of the Lich", "of the Necromancer", "of the Warlock", "of the Sorcerer", "of the Wizard", "of the Mage", "of the Alchemist", "of the Enchanter", "of the Illusionist", "of the Elementalist", "of the Pyromancer", "of the Cryomancer", "of the Geomancer", "of the Aeromancer", "of the Hydromancer", "of the Chronomancer", "of the Necromancer", "of the Summoner"]

    if type = "Heavy":
        Material = ["Steel", "Iron", "Bronze", "Titanium", "Adamantium", "Obsidian", "Dragonhide"]
    elif type = "Medium":
        Material = ["Composite", "Plate","Composite", "Plate", "Scale Mail", "Brigandine", "Lamellar", "Cuirass", "Hauberk", "Studded Leather"]
    elif type = "Light":
        Material = ["Leather", "Bone", "Hide", "Fur", "Scale", "Chainmail"]
    elif type = "Cloth":
        Material = ["Cotton", "Linen", "Wool", "Silk", "Velvet", "Satin", "Brocade"]

    if slot = "Head":
        slotname = random.choice(["Helm", "Crown", "Cap", "Mask"])
    elif slot = "Shoulder":
        slotname = random.choice(["Pauldrons", "Spaulders", "Shoulder Guards", "Shoulder Pads", "Shoulder Plates", "Shoulder Armor", "Shoulder Capes", "Shoulder Cloaks"])
    elif slot = "Arm":
        slotname = random.choice(["Bracers", "Arm Guards", "Bicep Guards", "Sleeves", "Vambraces", "Cuffs", "Armlets"])
    elif slot = "Hand":
        slotname = random.choice(["Gloves", "Gauntlets", "Mittens"])
    elif slot = "Chest":
        slotname = random.choice(["Chestplate", "Cuirass", "Hauberk"])
    elif slot = "Pants":
        slotname = random.choice(["Leggings", "Pants", "Trousers"])
    elif slot = "Boots":
        slotname = random.choice(["Boots", "Shoes", "Sandals"])

    # Choose a random prefix and suffix
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)

    # Combine them with the type and slot to create the item name
    return f"{prefix} {type} {slot} {suffix}"
