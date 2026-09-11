from datetime import datetime, timezone

from flask import abort, make_response
from marshmallow import ValidationError

from config import db
from models import Player, player_schema, players_schema


def get_timestamp():
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def read_all():
    """
    Read all players in PLAYERS
    """
    players = Player.query.all()
    return players_schema.dump(players)


def add(player):
    """
    Add player to PLAYERS
    """
    lname = player.get("lname")
    normalized_lname = normalize_name(lname)

    if lname != normalized_lname:
        abort(400, "lname in the request body must be capitalized")

    existing_player = Player.query.filter(
        Player.lname == normalized_lname
    ).one_or_none()

    if existing_player is not None:
        abort(406, f"Player with last name {lname} already exists")

    try:
        new_player = player_schema.load(player, session=db.session())
    except ValidationError as err:
        abort(400, err.messages)

    db.session.add(new_player)
    db.session.commit()

    return player_schema.dump(new_player), 201


def normalize_name(lname: str):
    """
    Normalizes lname argument to be capitalized ie ("Smith")
    """
    return lname.strip().lower().capitalize()


def read_one(lname: str):
    """
    Read one player from PLAYERS
    """
    normalized_lname = normalize_name(lname)

    player = Player.query.filter(Player.lname == normalized_lname).one_or_none()

    if player is None:
        abort(404, f"Player with last name {lname} not found")

    return player_schema.dump(player)


def update_one(lname: str, player_update: dict):
    """
    Update one player in PLAYERS
    """
    normalized_lname = normalize_name(lname)

    if "lname" in player_update and player_update["lname"] != normalized_lname:
        abort(400, "lname in the request body must be capitalized")

    existing_player = Player.query.filter(
        Player.lname == normalized_lname
    ).one_or_none()

    if existing_player is None:
        abort(404, f"Player with last name {lname} not found")

    try:
        player_update_validated = player_schema.load(
            player_update, session=db.session(), partial=True
        )
    except ValidationError as err:
        abort(400, err.messages)

    for key in player_update:
        setattr(existing_player, key, getattr(player_update_validated, key))

    existing_player.timestamp = get_timestamp()
    db.session.commit()

    return player_schema.dump(existing_player), 201


def delete_one(lname: str):
    """
    Delete one player in PLAYERS
    """
    normalized_lname = normalize_name(lname)
    existing_player = Player.query.filter(
        Player.lname == normalized_lname
    ).one_or_none()

    if existing_player is None:
        abort(400, f"Player with last name {lname} not found")

    db.session.delete(existing_player)
    db.session.commit()

    return make_response(f"{lname} successfully deleted", 200)
