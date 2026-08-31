import sqlite3

conn = sqlite3.connect("players.db")

columns = [
    "id INTEGER PRIMARY KEY AUTOINCREMENT",
    "fname TEXT NOT NULL",
    "lname TEXT NOT NULL UNIQUE",
    "birth_date DATE NOT NULL",
    "country TEXT NOT NULL",
    "dominant_hand TEXT NOT NULL CHECK (dominant_hand IN ('left', 'right'))",
    "backhand INTEGER NOT NULL CHECK (backhand IN (1, 2))",
    "timestamp TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now'))",
]
create_table_cmd = f"CREATE TABLE players ({','.join(columns)})"
conn.execute(create_table_cmd)
conn.commit()
conn.close()
