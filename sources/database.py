import sqlite3

DB_PATH = "backrooms.db"

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS joueurs (
                pseudo  TEXT PRIMARY KEY,
                points  INTEGER DEFAULT 0
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS validations (
                pseudo  TEXT NOT NULL,
                niveau  INTEGER NOT NULL,
                UNIQUE(pseudo, niveau)
            )
        """)

        con.commit()

def ajouter_joueur(pseudo):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("INSERT OR IGNORE INTO joueurs (pseudo) VALUES (?)", (pseudo,))
        con.commit()

def valider_niveau(pseudo, niveau, points):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO validations (pseudo, niveau) VALUES (?, ?)",
            (pseudo, niveau)
        )
        if cur.rowcount > 0:  # 1ère fois qu'il valide ce niveau
            cur.execute(
                "UPDATE joueurs SET points = points + ? WHERE pseudo = ?",
                (points, pseudo)
            )
        con.commit()
        return cur.rowcount > 0  # True = nouveau, False = déjà fait

def get_niveaux_valides(pseudo):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT niveau FROM validations WHERE pseudo = ?", (pseudo,))
        return [row[0] for row in cur.fetchall()]  # ex: [0, 1]

def get_leaderboard():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT pseudo, points FROM joueurs ORDER BY points DESC")
        return cur.fetchall()