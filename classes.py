#!/usr/bin/env python

# Import built-in libraries
import sqlite3
from dataclasses import dataclass, field

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


@dataclass
class Hand:

    item: str
    weakness: str = field(init=False)
    strength: str = field(init=False)
    points: int = field(init=False)


    def get_property(self, item_property: str, item_name: str) -> str | int:
        with connection:
            cursor.execute(f"""SELECT {item_property} FROM 'Properties'
                            WHERE Name IS ?""", (item_name,))
            return cursor.fetchone()[0]


    def __post_init__(self):
        self.weakness = self.get_property("Weakness", self.item)
        self.strength = self.get_property("Strength", self.item)
        self.points = self.get_property("Points", self.item)
