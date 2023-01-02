#!/usr/bin/env python

# Import custom libraries
from classes import Hand


def decode(cyphertext: str):
    _plaintext: str = ""

    # TODO: use TOML file for configuration
    # NOTE: implementing above TODO increases code reuse
    codec: dict = {
        "rock": {"A", "X"},
        "paper": {"B", "Y"},
        "scissor": {"C", "Z"}
    }

    if cyphertext in codec["rock"]:
        _plaintext = "rock"
    elif cyphertext in codec["paper"]:
        _plaintext = "paper"
    elif cyphertext in codec["scissor"]:
        _plaintext = "scissor"

    return _plaintext


# TODO: use argparse to allow custom data file input
with open("./data.txt", "r") as file:
    data = file.read().splitlines()

score: int = 0
round: str
for round in data:
    column_a: str
    column_b: str
    column_a, column_b = round.split(" ")
    opponent_hand = Hand(decode(column_a))
    player_hand = Hand(decode(column_b))

    score += player_hand.points

    if player_hand.weakness == opponent_hand.item:  # Loss
        score += 0
    elif player_hand.strength == opponent_hand.item:  # Win
        score += 6
    else:  # Tie
        score += 3

print(f"Final score: {score}")
