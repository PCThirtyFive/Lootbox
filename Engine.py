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
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT uid, name, rating FROM players")
    players = cursor.fetchall()

    for uid, name, rating in players:
        cursor.execute(
            "INSERT INTO stats (uid, name, wins, losses, rating) VALUES (?, ?, ?, ?, ?)",
            (uid, name, 0, 0, rating),
        )
    conn.commit()
    conn.close()


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
    players.append(player1id)

    return player1id, player2id

def Damagepool(type2):
    pooln=random.randint(1,100)
    if type2 == "Launcher":
        return random.choice(["Headhit", "Shoulderhit", "Bodyhit", "Armhit", "Handhit", "Leghit", "FootHit"])

    elif type2 == "Rifle" or "Warhammer" or "Axe" or "Greatsword" or "Longbow":
        if pooln > 45:
            return random.choice(["Headhit", "Shoulderhit"])
        elif pooln > 25:
            return random.choice(["Bodyhit", "Armhit", "Handhit"])
        else:
            return random.choice(["Leghit", "FootHit"])

    elif type2 == "Carbine" or "Bow" or "Polearm" or "Lance" or "Spear":
        if pooln > 45:
            return random.choice(["Leghit", "FootHit"])
        elif pooln > 25:
            return random.choice(["Bodyhit", "Armhit", "Handhit"])
        else:
            return random.choice(["Shoulderhit", "Headhit"])

    elif type2 == "Pistol" or "Dagger" or "Blade" or "Sword" or "Crossbow":
        if pooln > 45:
            return random.choice(["Bodyhit", "Armhit", "Handhit"])
        elif pooln > 17:
            return random.choice(["Leghit", "FootHit"])
        else:
            return random.choice(["Shoulderhit", "Headhit"])

    elif type2 == "Duster" or "Knuckler" or "Fist":
        if pooln > 60:
            return random.choice(["Bodyhit", "Armhit", "Handhit"])
        elif pooln > 20:
            return random.choice(["Shoulderhit", "Headhit"])
        else:
            return random.choice(["Leghit", "FootHit"])
def obtainplayerdata():
    players = get_players()
    player1id = players[0]
    player2id = players[1]
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    #get weapondata
    cursor.execute("SELECT AP, type2, Mindmg, Maxdmg, Speed, dmgtype, critchance, critdamage, name FROM weapons WHERE owner = ?", (player1id,))
    playeroneweaponex = cursor.fetchone()
    player1wpn = {"AP": playeroneweaponex[0], "Type": playeroneweaponex[1], "MinDmg": playeroneweaponex[2], "MaxDmg": playeroneweaponex[3], "Speed": playeroneweaponex[4], "DmgType": playeroneweaponex[5], "CritChance": playeroneweaponex[6], "CritDamage": playeroneweaponex[7], "Name": playeroneweaponex[8]}
    cursor.execute("SELECT AP, type2, Mindmg, Maxdmg, Speed, dmgtype, critchance, critdamage, name FROM weapons WHERE owner = ?", (player2id,))
    playertwoweaponex = cursor.fetchone()
    player2wpn = {"AP": playertwoweaponex[0], "Type": playertwoweaponex[1], "MinDmg": playertwoweaponex[2], "MaxDmg": playertwoweaponex[3], "Speed": playertwoweaponex[4], "DmgType": playertwoweaponex[5], "CritChance": playertwoweaponex[6], "CritDamage": playertwoweaponex[7], "Name": playertwoweaponex[8]}
    #get player data
    cursor.execute("SELECT hp, name, rating, encumberance FROM players WHERE uid = ?", (player1id,))
    p1results = cursor.fetchone()
    player1hp = p1results[0]
    player1name = p1results[1]
    p1rating = p1results[2]
    cursor.execute("SELECT hp, name, rating,encumberance FROM players WHERE uid = ?", (player2id,))
    p2results = cursor.fetchone()
    player2hp = p2results[0]
    player2name = p2results[1]
    p2rating = p2results[2]
    p1encumberance = p1results[3]
    p2encumberance = p2results[3]

    #get stats data
    cursor.execute("SELECT wins, losses FROM stats WHERE uid = ?", (player1id,))
    p1stats= cursor.fetchone()
    p1wins = int(p1stats[0])
    p1losses = int(p1stats[1])
    cursor.execute("SELECT wins, losses FROM stats WHERE uid = ?", (player2id,))
    p2results = cursor.fetchone()
    p2wins = int(p2results[0])
    p2losses = int(p2results[1])

    conn.close()
    return (player1id, player2id, player1wpn, player2wpn, player1hp, player2hp, player1name, player2name,
            p1rating, p2rating, p1wins, p1losses, p2wins, p2losses,p1encumberance, p2encumberance)

def damagecalc(attackerid, attackerwpn, defenderid):
    crit = 0

    if attackerwpn["AP"] == "Heavy":
        attAP = 4
    elif attackerwpn["AP"] == "Medium":
        attAP = 3
    elif attackerwpn["AP"] == "Light":
        attAP = 2
    elif attackerwpn["AP"] == "None":
        attAP = 1

    basedamage = random.randint(attackerwpn["MinDmg"], attackerwpn["MaxDmg"])
    critcheck = random.randint(1, 100)
    if critcheck <= attackerwpn["CritChance"]:
        crit = 1
    if crit == 1:
        basedamage = (basedamage * (attackerwpn["CritDamage"] / 100)) + basedamage

    slotpool = Damagepool(attackerwpn["Type"])
    if slotpool == "Headhit":
        slotdef = "Head"
    elif slotpool == "Shoulderhit":
        slotdef = "Shoulder"
    elif slotpool == "Bodyhit":
        slotdef = "Chest"
    elif slotpool == "Armhit":
        slotdef = "Arm"
    elif slotpool == "Handhit":
        slotdef = "Hand"
    elif slotpool == "Leghit":
        slotdef = "Pants"
    elif slotpool == "FootHit":
        slotdef = "Boots"

    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    # Query player1 data
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln, name FROM armour WHERE owner = ? and slot = ?", (defenderid, slotdef,))
    defenderdata = cursor.fetchone()
    armapdef = defenderdata[0]
    if defenderdata[1] is None:
        specproc = ["Nil"]
    else:    # Convert JSON string to Python object
        specproc = json.loads(defenderdata[1])
    specres = defenderdata[2]
    baseres = defenderdata[3]
    if defenderdata[4] is None:
        vuln = ["Nil"]
    else:
        vuln = json.loads(defenderdata[4]) if not None else ["Nil"]
    aname = defenderdata[5]
    conn.close()

    #calc resistance% to apply
    if attackerwpn["DmgType"] in specproc:
        armres = float((100 - specres) / 100)
    elif attackerwpn["DmgType"] in vuln:
        armres = 1
    else:
        armres = float((100 - baseres) / 100)

    APmulti = float(attAP / armapdef) #calc AP multiplier
    damage = int(basedamage * APmulti)
    absorbed = int(damage) - int(basedamage * APmulti * armres) #calc damage absorbed by armour
    HPloss = int(damage * armres) #calc HP loss
    return damage, crit, aname, absorbed, HPloss

def FightLoop():
    importeddata = obtainplayerdata()
    player2 = importeddata[1]
    player1 = importeddata[0]
    player1wpn = importeddata[2]
    player2wpn = importeddata[3]
    player1HP = importeddata[4]
    player2HP = importeddata[5]
    player1name = importeddata[6]
    player2name = importeddata[7]
    player1TurnSpeed = 1
    player2TurnSpeed = 1
    Turn = 1
    p1wn = player1wpn["Name"]
    p2wn = player2wpn["Name"]
    p1rating = importeddata[8]
    p2rating = importeddata[9]
    p1wins = importeddata[10]
    p1losses = importeddata[11]
    p2wins = importeddata[12]
    p2losses = importeddata[13]
    p1encumberance = importeddata[14]
    p2encumberance = importeddata[15]

    print(f"The next fight is between {player1name} rated at {p1rating} with a record of {p1wins} wins and {p1losses} losses")
    print(" ")
    print(f"and {player2name} rated at {p2rating} with a record of {p2wins} wins and {p2losses} losses")
    print(" ")
    print("The fight will begin in 1 minute")
    time.sleep(0)

    while player1HP > 1 and player2HP > 1:
        if player1TurnSpeed == Turn or player1TurnSpeed < Turn:
            # Player 1's turn
            print(f"{player1name}s turn")
            time.sleep(0)
            print(f"Attacking with {p1wn}")
            time.sleep(0)
            results = damagecalc(player1, player1wpn, player2)
            damage = results[0]
            crit = "Critically hits for" if results[1] == 1 else "hits for"
            print(f"{player1name} {crit} {results[0]} {player1wpn["DmgType"]} damage to {player2name}")
            time.sleep(0)
            print(f"{player2name}'s {results[2]} absorbs {results[3]} damage")
            time.sleep(0)
            print(f"{player2name} loses {results[4]} HP")
            player2HP -= results[4]
            print(f"{player2name} has {player2HP} HP left")
            time.sleep(0)
            #add player turnspeed
            player1TurnSpeed += player1wpn["Speed"] + p1encumberance
            if player2HP <= 0:
                print(f"{player2name} has been defeated")
                winner = player1name
                loser = player2name
                conn = sqlite3.connect("game.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE stats SET wins = wins + 1 WHERE uid = ?", (player1,))
                cursor.execute("UPDATE stats SET losses = losses + 1 WHERE uid = ?", (player2,))
                conn.commit()
                conn.close()
                break
        elif player1TurnSpeed > Turn:
            print(f"{player1name} is preparing their attack")
            time.sleep(0)

        # Player 2's turn
        if player2TurnSpeed == Turn or player2TurnSpeed < Turn:
            print(f"{player2name}s turn")
            time.sleep(0)
            print(f"Attacking with {p2wn}")
            time.sleep(0)
            results = damagecalc(player2, player2wpn, player1)
            damage = results[0]
            crit = "Critically hits for" if results[1] == 1 else "hits for"

            print(f"{player2name} {crit} {results[0]} {player2wpn["DmgType"]} damage to {player1name}")
            time.sleep(0)
            print(f"{player1name}'s {results[2]} absorbs {results[3]} damage")
            time.sleep(0)
            print(f"{player1name} loses {results[4]} HP")
            player1HP -= results[4]
            print(f"{player1name} has {player1HP} HP left")
            time.sleep(0)
            player2TurnSpeed += player2wpn["Speed"] + p2encumberance
            if player1HP <= 0:
                print(f"{player1name} has been defeated")
                loser = player1name
                winner = player2name
                conn = sqlite3.connect("game.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE stats SET wins = wins + 1 WHERE uid = ?", (player2,))
                cursor.execute("UPDATE stats SET losses = losses + 1 WHERE uid = ?", (player1,))
                conn.commit()
                conn.close()
                break
        elif player2TurnSpeed > Turn:
            print(f"{player2name} is preparing their attack")
            time.sleep(0)
        Turn += 1

    print(f"{winner} has defeated {loser}")
    time.sleep(1)
    FightLoop()

FightLoop()



