#!/usr/bin/env python

# Import built-in libraries
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# TODO: consider making this a dataclass
class Hand:

    def get_property(self, item_property: str, item_name: str) -> str | int:
        with connection:
            cursor.execute(f"""SELECT {item_property} FROM 'Properties'
                            WHERE Name IS ?""", (item_name,))
            return cursor.fetchone()[0]

    def __init__(self, item: str):
        self.item: str = item
        self.weakness: str = self.get_property("Weakness", self.item)
        self.strength: str = self.get_property("Strength", self.item)
        self.points: int = self.get_property("Points", self.item)
