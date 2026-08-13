from datetime import datetime, timezone


def get_timestamp():
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


PLAYERS = {
    "Fritz": {
        "fname": "Taylor",
        "lname": "Fritz",
        "born": "1997-10-28",
        "country": "USA",
        "birthplace": "Rancho Santa Fe",
        "dominant_hand": "right",
        "backhand": "two",
        "timestamp": get_timestamp(),
    },
    "Shelton": {
        "fname": "Ben",
        "lname": "Shelton",
        "born": "2002-10-09",
        "country": "USA",
        "birthplace": "Atlanta",
        "dominant_hand": "left",
        "backhand": "two",
        "timestamp": get_timestamp(),
    },
    "Tiafoe": {
        "fname": "Francis",
        "lname": "Tiafoe",
        "born": "1998-01-20",
        "country": "USA",
        "birthplace": "Hyattsville",
        "dominant_hand": "right",
        "backhand": "two",
        "timestamp": get_timestamp(),
    },
    "Paul": {
        "fname": "Tommy",
        "lname": "Paul",
        "born": "1997-05-17",
        "country": "USA",
        "birthplace": "Voorhees",
        "dominant_hand": "right",
        "backhand": "two",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return list(PLAYERS.values())
