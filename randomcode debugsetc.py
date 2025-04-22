'''#debug the rating:
# Debug logging for intermediate values
specres_adjusted = (self.specres - 75) / 20
baseres_adjusted = (self.baseres - 45) / 30
combined_res = (specres_adjusted + baseres_adjusted) / 50 * 2
specproc_component = specproc_count / 3
baseproc_component = (basecount + specproc_count) / 13

# Log intermediate values
print(f"specres_adjusted: {specres_adjusted}")
print(f"baseres_adjusted: {baseres_adjusted}")
print(f"combined_res: {combined_res}")
print(" ")
print(f"specproc_count: {specproc_count}")
print(f"basecount: {basecount}")
print(f"specproc_component: {specproc_component}")
print(f"baseproc_component: {baseproc_component}")


# Calculate the rating
self.rating = int(((combined_res + specproc_component + baseproc_component) / 4) * 100)

# Log final rating before capping
print(f"Calculated rating before capping: {self.rating}")

# Cap the rating at 100
self.rating = min(self.rating, 100)'''

import random
import string

def generate_random_string():
    """Generates a random string of letters and numbers with the specified length."""
    length=25
    characters = string.ascii_letters + string.digits  # Combine letters and digits
    return ''.join(random.choices(characters, k=length))

# Example usage
for _ in range(10):
    random_string = generate_random_string()
    print(random_string)



    '''  #get armour data
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln, FROM armour WHERE owner = ? and slot = ?", (player1id, p1arm))
    p1armd = cursor.fetchall()
    p1armdata = {"Slot": "Arm", "TypeVal": p1armd[0], "SpecProc": json.loads(p1armd[1]), "SpecRes": p1armd[2], "BaseRes": p1armd[3], "Vuln": json.loads(p1armd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1hand))
    p1handd = cursor.fetchall()
    p1handdata = {"Slot": "Hand", "TypeVal": p1handd[0], "SpecProc": json.loads(p1handd[1]), "SpecRes": p1handd[2], "BaseRes": p1handd[3], "Vuln": json.loads(p1handd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1chest))
    p1chestd = cursor.fetchall()
    p1chestdata = {"Slot": "Chest", "TypeVal": p1chestd[0], "SpecProc": json.loads(p1chestd[1]), "SpecRes": p1chestd[2], "BaseRes": p1chestd[3], "Vuln": json.loads(p1chestd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1pants))
    p1pantsd = cursor.fetchall()
    p1pantsdata = {"Slot": "Pants", "TypeVal": p1pantsd[0], "SpecProc": json.loads(p1pantsd[1]), "SpecRes": p1pantsd[2], "BaseRes": p1pantsd[3], "Vuln": json.loads(p1pantsd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1boots))
    p1bootsd = cursor.fetchall()
    p1bootsdata = {"Slot": "Boots", "TypeVal": p1bootsd[0], "SpecProc": json.loads(p1bootsd[1]), "SpecRes": p1bootsd[2], "BaseRes": p1bootsd[3], "Vuln": json.loads(p1bootsd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1head))
    p1headd = cursor.fetchall()
    p1headdata = {"Slot": "Head", "TypeVal": p1headd[0], "SpecProc": json.loads(p1headd[1]), "SpecRes": p1headd[2], "BaseRes": p1headd[3], "Vuln": json.loads(p1headd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player1id, p1shoulder))
    p1shoulderd = cursor.fetchall()
    p1shoulderdata = {"Slot": "Shoulder", "TypeVal": p1shoulderd[0], "SpecProc": json.loads(p1shoulderd[1]), "SpecRes": p1shoulderd[2], "BaseRes": p1shoulderd[3], "Vuln": json.loads(p1shoulderd[4])}

    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln, FROM armour WHERE owner = ? and slot = ?", (player2id, p2arm))
    p2armd = cursor.fetchall()
    p2armdata = {"Slot": "Arm", "TypeVal": p2armd[0], "SpecProc": json.loads(p2armd[1]), "SpecRes": p2armd[2], "BaseRes": p2armd[3], "Vuln": json.loads(p2armd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2hand))
    p2handd = cursor.fetchall()
    p2handdata = {"Slot": "Hand", "TypeVal": p2handd[0], "SpecProc": json.loads(p2handd[1]), "SpecRes": p2handd[2], "BaseRes": p2handd[3], "Vuln": json.loads(p2handd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2chest))
    p2chestd = cursor.fetchall()
    p2chestdata = {"Slot": "Chest", "TypeVal": p2chestd[0], "SpecProc": json.loads(p2chestd[1]), "SpecRes": p2chestd[2], "BaseRes": p2chestd[3], "Vuln": json.loads(p2chestd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2pants))
    p2pantsd = cursor.fetchall()
    p2pantsdata = {"Slot": "Pants", "TypeVal": p2pantsd[0], "SpecProc": json.loads(p2pantsd[1]), "SpecRes": p2pantsd[2], "BaseRes": p2pantsd[3], "Vuln": json.loads(p2pantsd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2boots))
    p2bootsd = cursor.fetchall()
    p2bootsdata = {"Slot": "Boots", "TypeVal": p2bootsd[0], "SpecProc": json.loads(p2bootsd[1]), "SpecRes": p2bootsd[2], "BaseRes": p2bootsd[3], "Vuln": json.loads(p2bootsd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2head))
    p2headd = cursor.fetchall()
    p2headdata = {"Slot": "Head", "TypeVal": p2headd[0], "SpecProc": json.loads(p2headd[1]), "SpecRes": p2headd[2], "BaseRes": p2headd[3], "Vuln": json.loads(p2headd[4])}
    cursor.execute("SELECT typeval, specproc, specres, baseres, vuln FROM armour WHERE owner = ? and slot = ?", (player2id, p2shoulder))
    p2shoulderd = cursor.fetchall()
    p2shoulderdata = {"Slot": "Shoulder", "TypeVal": p2shoulderd[0], "SpecProc": json.loads(p2shoulderd[1]), "SpecRes": p2shoulderd[2], "BaseRes": p2shoulderd[3], "Vuln": json.loads(p2shoulderd[4])}'''

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