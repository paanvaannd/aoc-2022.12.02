#!/usr/bin/env python

class Hand:

    # TODO: replace with SQLite query on tabulated data
    def get_weakness(self, item):
        _weakness = ""
        if item == "rock":
            _weakness = "paper"
        elif item == "paper":
            _weakness = "scissor"
        elif item == "scissor":
            _weakness = "rock"
        return _weakness

    # TODO: replace with SQLite query on tabulated data
    def get_strength(self, item):
        _strength = ""
        if item == "rock":
            _strength = "scissor"
        elif item == "paper":
            _strength = "rock"
        elif item == "scissor":
            _strength = "paper"
        return _strength
    
    # TODO: replace with SQLite query on tabulated data
    def get_points(self, item):
        _points = 0
        if item == "rock":
            _points = 1
        if item == "paper":
            _points = 2
        if item == "scissor":
            _points = 3
        return _points

    def __init__(self, item):
        self.item = item
        self.weakness = self.get_weakness(self.item)
        self.strength = self.get_strength(self.item)
        self.points = self.get_points(self.item)
