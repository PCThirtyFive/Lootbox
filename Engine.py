import random
import Database
import sqlite3
import time
import json
import PlayerGen
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
    cursor.execute("SELECT head, shoulder, chest, arm, hand, pants, boots, mainhand, rating FROM players WHERE uid = ?", (player1id,))
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
    Player1Items = {"Head": p1head, "Shoulder": p1shoulder, "Arm": p1arm, "Hand": p1hand, "Chest": p1chest, "Pants": p1pants, "Boots": p1boots, "Mainhand": p1mainhand, "Rating": p1rating}
    # Query player2 data
    cursor.execute("SELECT head, shoulder, chest, arm, hand, pants, boots, mainhand, rating FROM players WHERE uid = ?", (player2id,))
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
    Player2Items = {"Head": p2head, "Shoulder": p2shoulder, "Arm": p2arm, "Hand": p2hand, "Chest": p2chest, "Pants": p2pants, "Boots": p2boots, "Mainhand": p2mainhand, "Rating": p2rating}
    return Player1Items, Player2Items, player1id, player2id


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



def Fight():
    importeddata = obtainplayerdata()
    player1items = importeddata[0]
    player2items = importeddata[1]
    player2 = importeddata[3]
    player1 = importeddata[2]



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





