import sqlite3

PLAYERS = {
    "Fritz": {
        "fname": "Taylor",
        "lname": "Fritz",
        "birth_date": "1997-10-28",
        "country": "USA",
        "dominant_hand": "right",
        "backhand": 2,
    },
    "Shelton": {
        "fname": "Ben",
        "lname": "Shelton",
        "birth_date": "2002-10-09",
        "country": "USA",
        "dominant_hand": "left",
        "backhand": 2,
    },
    "Tiafoe": {
        "fname": "Francis",
        "lname": "Tiafoe",
        "birth_date": "1998-01-20",
        "country": "USA",
        "dominant_hand": "right",
        "backhand": 2,
    },
    "Paul": {
        "fname": "Tommy",
        "lname": "Paul",
        "birth_date": "1997-05-17",
        "country": "USA",
        "dominant_hand": "right",
        "backhand": 2,
    },
}


INSERT_CMD = """
    INSERT OR IGNORE INTO players
        (lname, fname, birth_date, country, dominant_hand, backhand)
    VALUES
        (:lname, :fname, :birth_date, :country, :dominant_hand, :backhand)
"""


def seed():
    with sqlite3.connect("players.db") as conn:
        conn.executemany(INSERT_CMD, PLAYERS.values())
        print(f"Seeded {len(PLAYERS)} players into players.db")


if __name__ == "__main__":
    seed()
