from flask_marshmallow import sqla
from sqlalchemy import CheckConstraint, text
from sqlalchemy.engine.reflection import sql

import players
from config import db, ma


class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(32), nullable=False)
    lname = db.Column(db.String(32), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(32), nullable=False)
    dominant_hand = db.Column(db.String(32), nullable=False)
    backhand = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(
        db.String,
        nullable=False,
        server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now')"),
    )

    __table_args__ = (
        CheckConstraint(
            "dominant_hand IN ('left', 'right')", name="check_dominant_hand"
        ),
        CheckConstraint("backhand IN (1, 2)", name="check_backhand"),
    )


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        load_instance = True
        sqla_session = db.session


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
