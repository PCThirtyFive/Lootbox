import sqlite3
import hashlib


class UserDatabase:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self):
        """Create the necessary tables if they do not exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            pin TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def register_user(self, username, password, email, pin):
        """Register a new user."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, email, pin) VALUES (?, ?, ?, ?)",
                           (username, hashed_password, email, pin))
            player_id = cursor.lastrowid  # Retrieve the newly generated player ID
            conn.commit()
            conn.close()

            game_db = GameDatabase()
            game_db.add_player(player_id, username)  # Register player in game_data database

            return True
        except sqlite3.IntegrityError:
            return False

    def validate_login(self, username, password):
        """Validate user login credentials."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = cursor.fetchone()
        conn.close()
        return user is not None

    def retrieve_account(self, email, pin):
        """Retrieve account details for account recovery."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE email = ? AND pin = ?", (email, pin))
        user = cursor.fetchone()
        conn.close()
        return user[0] if user else None
