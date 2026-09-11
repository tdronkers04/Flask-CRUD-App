import pathlib
from typing import cast

import connexion
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=basedir)

app = cast(Flask, connexion_app.app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'players.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
