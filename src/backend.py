import sqlite3, os, time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "stats.db")

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

class Cardinal:
    
    @staticmethod
    def init_db():
        
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_anime TEXT,
                saison INTEGER,
                episode INTEGER,
                date_utilisation TEXT,
                timestamp INTEGER
            )
        """)
        conn.commit()
        conn.close()


    def statCollect(nom_anime, saison_num, num_episode):
        jour = datetime.now().strftime("%Y-%m-%d")
        timestamp = int(time.time())

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("""
            INSERT INTO stats (nom_anime, saison, episode, date_utilisation, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (nom_anime, saison_num, num_episode, jour, timestamp))

        conn.commit()
        conn.close()

    def getStats(p):
        time.sleep(1.5)
        if p == ADMIN_PASSWORD:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()

            # c.execute("SELECT nom_anime, saison, episode, date_utilisation, timestamp FROM stats")
            c.execute("SELECT * FROM stats")
            rows = c.fetchall()

            conn.close()

            return rows
        else:
            return "Satus DB : OK"