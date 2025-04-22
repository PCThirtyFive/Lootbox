import random
import Database
import sqlite3
import time
import json
import PlayerGen

def generateplayers():
    for _ in range (50):
        PlayerGen.HumanPlayer()
        PlayerGen.cpuplayer()
        FightLoop()
def get_players():
    """
    Prints each player's name, armour name and rating, and weapon name and rating.
    """
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    # Query all players
    cursor.execute("SELECT uid FROM players")
    playertuples = cursor.fetchall()

    players = [player_tuple[0] for player_tuple in playertuples]

    player1id = str(random.choice(players))
    players.remove(player1id)
    player2id = str(random.choice(players))
    players.remove(player2id)
    PlayerGen.HumanPlayer()
    PlayerGen.cpuplayer()
    return player1id, player2id


def obtainplayerdata():
    players = get_players()
    player1id = players[0]
    player2id = players[1]
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    # Query player1 data
    cursor.execute("SELECT head, shoulder, chest, arm, hand, pants, boots, mainhand, rating, hp FROM players WHERE uid = ?", (player1id,))
    player1data = cursor.fetchone()
    p1head = player1data[0]
    p1shoulder = player1data[1]
    p1arm = player1data[2]
    p1hand = player1data[3]
    p1chest = player1data[4]
    p1pants = player1data[5]
    p1boots = player1data[6]
    p1mainhand = player1data[7]
    p1rating = player1data[8]
    p1hp = player1data[9]
    Player1Items = {"Head": p1head, "Shoulder": p1shoulder, "Arm": p1arm, "Hand": p1hand, "Chest": p1chest, "Pants": p1pants, "Boots": p1boots, "Mainhand": p1mainhand, "Rating": p1rating, "HP": p1hp}
    # Query player2 data
    cursor.execute("SELECT head, shoulder, chest, arm, hand, pants, boots, mainhand, rating, hp FROM players WHERE uid = ?", (player2id,))
    player2data = cursor.fetchone()
    p2head = player2data[0]
    p2shoulder = player2data[1]
    p2arm = player2data[2]
    p2hand = player2data[3]
    p2chest = player2data[4]
    p2pants = player2data[5]
    p2boots = player2data[6]
    p2mainhand = player2data[7]
    p2rating = player2data[8]
    p2hp = player2data[9]
    Player2Items = {"Head": p2head, "Shoulder": p2shoulder, "Arm": p2arm, "Hand": p2hand, "Chest": p2chest, "Pants": p2pants, "Boots": p2boots, "Mainhand": p2mainhand, "Rating": p2rating, "HP": p2hp}
    cursor.execute("SELECT AP, type002, Mindmg, Maxdmg, Speed, dmgtype, critchance, critdamage FROM weapons WHERE owner = ?", (player1id,))

    #getweapon data
    playeroneweaponex = cursor.fetchone()
    player1wpn = {"AP": playeroneweaponex[0], "Type": playeroneweaponex[1], "MinDmg": playeroneweaponex[2], "MaxDmg": playeroneweaponex[3], "Speed": playeroneweaponex[4], "DmgType": playeroneweaponex[5], "CritChance": playeroneweaponex[6], "CritDamage": playeroneweaponex[7]}
    cursor.execute("SELECT AP, type002, Mindmg, Maxdmg, Speed, dmgtype, critchance, critdamage FROM weapons WHERE owner = ?", (player2id,))
    playertwoweaponex = cursor.fetchone()
    player2wpn = {"AP": playertwoweaponex[0], "Type": playertwoweaponex[1], "MinDmg": playertwoweaponex[2], "MaxDmg": playertwoweaponex[3], "Speed": playertwoweaponex[4], "DmgType": playertwoweaponex[5], "CritChance": playertwoweaponex[6], "CritDamage": playertwoweaponex[7]}

    #get armour data
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln, FROM armour WHERE owner = ? and slot = ?", (player1id, p1arm))
    p1armd = cursor.fetchall()
    p1armdata = {"Slot": "Arm", "TypeVal": p1armd[0], "SpecProc": p1armd[1], "SpecRes": p1armd[2], "BaseRes": p1armd[3], "Vuln": p1armd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1hand))
    p1handd = cursor.fetchall()
    p1handdata = {"Slot": "Hand", "TypeVal": p1handd[0], "SpecProc": p1handd[1], "SpecRes": p1handd[2], "BaseRes": p1handd[3], "Vuln": p1handd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1chest))
    p1chestd = cursor.fetchall()
    p1chestdata = {"Slot": "Chest", "TypeVal": p1chestd[0], "SpecProc": p1chestd[1], "SpecRes": p1chestd[2], "BaseRes": p1chestd[3], "Vuln": p1chestd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1pants))
    p1pantsd = cursor.fetchall()
    p1pantsdata = {"Slot": "Pants", "TypeVal": p1pantsd[0], "SpecProc": p1pantsd[1], "SpecRes": p1pantsd[2], "BaseRes": p1pantsd[3], "Vuln": p1pantsd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1boots))
    p1bootsd = cursor.fetchall()
    p1bootsdata = {"Slot": "Boots", "TypeVal": p1bootsd[0], "SpecProc": p1bootsd[1], "SpecRes": p1bootsd[2], "BaseRes": p1bootsd[3], "Vuln": p1bootsd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1head))
    p1headd = cursor.fetchall()
    p1headdata = {"Slot": "Head", "TypeVal": p1headd[0], "SpecProc": p1headd[1], "SpecRes": p1headd[2], "BaseRes": p1headd[3], "Vuln": p1headd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1shoulder))
    p1shoulderd = cursor.fetchall()
    p1shoulderdata = {"Slot": "Shoulder", "TypeVal": p1shoulderd[0], "SpecProc": p1shoulderd[1], "SpecRes": p1shoulderd[2], "BaseRes": p1shoulderd[3], "Vuln": p1shoulderd[4]}

    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln, FROM armour WHERE owner = ? and slot = ?", (player2id, p2arm))
    p2armd = cursor.fetchall()
    p2armdata = {"Slot": "Arm", "TypeVal": p2armd[0], "SpecProc": p2armd[1], "SpecRes": p2armd[2], "BaseRes": p2armd[3], "Vuln": p2armd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2hand))
    p2handd = cursor.fetchall()
    p2handdata = {"Slot": "Hand", "TypeVal": p2handd[0], "SpecProc": p2handd[1], "SpecRes": p2handd[2], "BaseRes": p2handd[3], "Vuln": p2handd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2chest))
    p2chestd = cursor.fetchall()
    p2chestdata = {"Slot": "Chest", "TypeVal": p2chestd[0], "SpecProc": p2chestd[1], "SpecRes": p2chestd[2], "BaseRes": p2chestd[3], "Vuln": p2chestd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2pants))
    p2pantsd = cursor.fetchall()
    p2pantsdata = {"Slot": "Pants", "TypeVal": p2pantsd[0], "SpecProc": p2pantsd[1], "SpecRes": p2pantsd[2], "BaseRes": p2pantsd[3], "Vuln": p2pantsd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2boots))
    p2bootsd = cursor.fetchall()
    p2bootsdata = {"Slot": "Boots", "TypeVal": p2bootsd[0], "SpecProc": p2bootsd[1], "SpecRes": p2bootsd[2], "BaseRes": p2bootsd[3], "Vuln": p2bootsd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2head))
    p2headd = cursor.fetchall()
    p2headdata = {"Slot": "Head", "TypeVal": p2headd[0], "SpecProc": p2headd[1], "SpecRes": p2headd[2], "BaseRes": p2headd[3], "Vuln": p2headd[4]}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2shoulder))
    p2shoulderd = cursor.fetchall()
    p2shoulderdata = {"Slot": "Shoulder", "TypeVal": p2shoulderd[0], "SpecProc": p2shoulderd[1], "SpecRes": p2shoulderd[2], "BaseRes": p2shoulderd[3], "Vuln": p2shoulderd[4]}

    return (Player1Items, Player2Items, player1id, player2id, player1wpn, player2wpn, p1armdata, p1handdata, p1chestdata,
            p1pantsdata, p1bootsdata, p1headdata, p1shoulderdata, p2armdata, p2handdata, p2chestdata, p2pantsdata,
            p2bootsdata, p2headdata, p2shoulderdata)


def Damagepool(type2):
    pooln=random.randint(1,100)
    if type2 == "Launcher":
        return "Spread"

    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        if pooln > 45:
            return random.choice("Headhit", "Shoulderhit")
        elif pooln > 25:
            return random.choice("Bodyhit", "Armhit", "Handhit")
        else:
            return random.choice("Leghit", "FootHit")

    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        if pooln > 45:
            return random.choice("Leghit", "FootHit")
        elif pooln > 25:
            return random.choice("Bodyhit", "Armhit", "Handhit")
        else:
            return random.choice("Shoulderhit", "Headhit")

    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        if pooln > 45:
            return random.choice("Bodyhit", "Armhit", "Handhit")
        elif pooln > 17:
            return random.choice("Leghit", "FootHit")
        else:
            return random.choice("Shoulderhit", "Headhit")

    elif type2 == "Duster" or "Knuckler" or "Fist":
        if pooln > 60:
            return random.choice("Bodyhit", "Armhit", "Handhit")
        elif pooln > 20:
            return random.choice("Shoulderhit", "Headhit")
        else:
            return random.choice("Leghit", "FootHit")




'''# Player stats
Player1Speed = 2

Player1Headslot = 1
Player1Shoulderslot = 2
Player1Armslot = 3
Player1Handslot = 4
Player1Chestslot = 5
Player1Pantslot = 6
Player1Bootsslot = 7
Player1Mainhandslot = 8
PLayer1Offhandslot = 9

Player2Speed = 2
Player2Headslot = 1
Player2Shoulderslot = 2
Player2Armslot = 3
Player2Handslot = 4
Player2Chestslot = 5
Player2Pantslot = 6
Player2Bootsslot = 7
Player2Mainhandslot = 8
Player2Offhandslot = 9

#engine for the game'''



def FightLoop():
    importeddata = obtainplayerdata()
    player1items = importeddata[0]
    player2items = importeddata[1]
    player2 = importeddata[3]
    player1 = importeddata[2]
    player1wpn = importeddata[4]
    player2wpn = importeddata[5]
    p1armdata = importeddata[6]
    p1handdata = importeddata[7]
    p1chestdata = importeddata[8]
    p1pantsdata = importeddata[9]
    p1bootsdata = importeddata[10]
    p1headdata = importeddata[11]
    p1shoulderdata = importeddata[12]
    p2armdata = importeddata[13]
    p2handdata = importeddata[14]
    p2chestdata = importeddata[15]
    p2pantsdata = importeddata[16]
    p2bootsdata = importeddata[17]
    p2headdata = importeddata[18]
    p2shoulderdata = importeddata[19]




    if player1items["Rating"] > player2items["Rating"]:
        attacker1 = player1
        attacker2= player2
    elif player2items["Rating"] > player1items["Rating:"]:
        attacker1 = player2
        attacker2 = player1
    else:
       attacker1 = random.choice([player1, player2])
       attacker2 = player1 if attacker1 == player2 else player2

    attacker1TurnSpeed = 1
    attacker2TurnSpeed = 1
    Turn = 1
    if attacker1

    while player1HP > 1 and player2HP > 1:
        if attacker1TurnSpeed == Turn or attacker1TurnSpeed < Turn:'''





