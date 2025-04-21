import sqlite3
import json


class Database:
    def __init__(self, db_name="game.db"):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

    #create a table for storing armour objects
        cursor.execute('''CREATE TABLE IF NOT EXISTS armour (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                slot TEXT,
                type TEXT,
                typeval INTEGER,
                specproc TEXT,
                specres INTEGER,
                baseproc TEXT,
                baseres INTEGER,
                vuln TEXT,
                condition INTEGER,
                socket INTEGER,
                modifiers1 TEXT,
                modifiers2 TEXT,
                modifiers1v INTEGER,
                modifiers2v INTEGER,
                setbonus TEXT,
                rating INTEGER,
                owner TEXT)''')
        conn.commit()
        conn.close()

    #create a table for storing weapon objects
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS weapons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                type2 TEXT,
                AP TEXT,
                dmgtype TEXT,
                Speed FLOAT,
                Accuracy INTEGER,
                Maxdmg INTEGER,
                Mindmg INTEGER,
                critchance INTEGER,
                critdamage INTEGER,
                slot TEXT,
                condition INTEGER,
                owner TEXT,
                special TEXT,
                rating INTEGER)''')
        conn.commit()
        conn.close()


Database()