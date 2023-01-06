#!/usr/bin/env python

# Import built-in libraries
import sqlite3

# Import custom libraries
from classes import Hand


def decode(cyphertext: str, codec: dict) -> str:
    # TODO: use TOML file for configuration
    # NOTE: implementing above TODO increases code reuse
    # TODO: find dynamic way to assign plaintext
    _plaintext: str
    if cyphertext in codec["rock"]:
        _plaintext = "rock"
    elif cyphertext in codec["paper"]:
        _plaintext = "paper"
    elif cyphertext in codec["scissor"]:
        _plaintext = "scissor"
    elif cyphertext in codec["lose"]:
        _plaintext = "lose"
    elif cyphertext in codec["draw"]:
        _plaintext = "draw"
    elif cyphertext in codec["win"]:
        _plaintext = "win"
    return _plaintext


def cheat(strategy: str, reference: Hand) -> str:
    player_choice: str
    if strategy == "lose":
        player_choice = reference.strength
    elif strategy == "win":
        player_choice = reference.weakness
    else:
        player_choice = reference.item
    return player_choice


assumed_codec: dict = {
    "rock": {"A", "X"},
    "paper": {"B", "Y"},
    "scissor": {"C", "Z"}
}

intended_codec: dict = {
    "rock": {"A"},
    "paper": {"B"},
    "scissor": {"C"},
    "lose": {"X"},
    "draw": {"Y"},
    "win": {"Z"},
}

# TODO: use argparse to allow custom data file input
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
with connection:
    cursor.execute("SELECT * FROM Input")
    data = cursor.fetchall()

for attempt in 1, 2:
    score: int = 0
    round: str
    for round in data:
        opponent_item: str
        player_item: str
        opponent_item, player_item = round

        opponent_hand = Hand(decode(opponent_item,
                                    assumed_codec if attempt == 1
                                    else intended_codec))
        player_hand = Hand(decode(player_item, assumed_codec) if attempt == 1
                           else cheat(decode(player_item, intended_codec),
                                      opponent_hand))

        score += player_hand.points

        if player_hand.weakness == opponent_hand.item:  # Loss
            score += 0
        elif player_hand.strength == opponent_hand.item:  # Win
            score += 6
        else:  # Tie
            score += 3

    print(f"Final score under {'assumed' if attempt == 1 else 'intended'} "
          f"interpretation of cheatsheet: {score}")
