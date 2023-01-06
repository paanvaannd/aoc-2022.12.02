#!/usr/bin/env python

# Import built-in libraries
import sqlite3
from configparser import ConfigParser

# Import custom libraries
from classes import Hand


def decode(cyphertext: str, codec: dict) -> str:
    _plaintext: str
    for key in codec:
        if key == cyphertext:
            return codec[key]


def cheat(strategy: str, reference: Hand) -> Hand:
    player_choice: Hand
    if strategy == "lose":
        player_choice = Hand(reference.strength)
    elif strategy == "win":
        player_choice = Hand(reference.weakness)
    else:
        player_choice = reference
    return player_choice


# TODO: use argparse to allow custom config file
cfg = ConfigParser()
cfg.read("config.ini")

connection = sqlite3.connect(str(cfg["DATABASE"]["filename"]))
cursor = connection.cursor()
with connection:
    cursor.execute("SELECT * FROM Input")
    data = cursor.fetchall()
    cursor.execute("SELECT Name FROM Properties")
    item_name_query_results = cursor.fetchall()
    item_names: list = []
    for result in item_name_query_results:
        item_names.append(str(result[0]))  # Ensure values are strings

score: int = 0
round: str
for round in data:
    opponent_cypher: str
    player_cypher: str
    opponent_cypher, player_cypher = round
    opponent_cypher = opponent_cypher.lower()
    player_cypher = player_cypher.lower()

    opponent_hand: Hand = Hand(decode(opponent_cypher, dict(cfg["CODEC"])))
    instructions: str = decode(player_cypher, dict(cfg["CODEC"]))
    player_hand: Hand
    if instructions not in set(item_names):
        player_hand = cheat(instructions, opponent_hand)
    else:
        player_hand = Hand(instructions)

    score += player_hand.points

    if player_hand.weakness == opponent_hand.item:  # Loss
        score += 0
    elif player_hand.strength == opponent_hand.item:  # Win
        score += 6
    else:  # Draw
        score += 3

print(f"Final score: {score}")
