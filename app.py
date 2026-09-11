from flask import render_template

import config
from models import Player

app = config.connexion_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    players = Player.query.all()
    return render_template("home.html", players=players)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
