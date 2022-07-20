from flask import render_template, request
from app import app
from models.rockpaperscissors import Game, Player
import random


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Home")


@app.route("/rps", methods=["GET", "POST"])
def rps():
    choice = request.form["choice"]
    name = request.form["name"]
    player = Player(name, choice)
    computer = Player("computer", random.choice(["rock", "paper", "scissors"]))
    game = Game(player, computer)
    return render_template("rps.html", title="Home", results=game.play())


@app.route("/<choice1>/<choice2>")
def play(choice1, choice2):
    player1 = Player("player1", choice1)
    player2 = Player("player2", choice2)
    game = Game(player1, player2)
    return render_template("rps.html", title="Home", results=game.play())
