import sqlite3

def print_player_details():
    """
    Prints each player's name, armour name and rating, and weapon name and rating.
    """
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    # Query all players
    cursor.execute("SELECT uid, name, rating FROM players")
    players = cursor.fetchall()

    for player in players:
        player_id, player_name, player_rating = player

        # Query player's armour
        cursor.execute("SELECT name, rating, slot FROM armour WHERE owner = ?", (player_id,))
        armour = cursor.fetchall()

        # Query player's weapon
        cursor.execute("SELECT name, rating FROM weapons WHERE owner = ?", (player_id,))
        weapons = cursor.fetchall()

        # Print player details
        print(f"Player: {player_name}")
        print (f"Rating: {player_rating}")
        print (" ")
        print("Armour:")
        for armour_name, armour_rating, armour_slot in armour:
            print(f"-{armour_slot}:\t{armour_name}:\t{armour_rating}")
        print("Weapons:")
        for weapon_name, weapon_rating in weapons:
            print(f"  - {weapon_name}: {weapon_rating}")
        print()

    conn.close()

# Call the function
print_player_details()