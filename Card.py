"""Module for the card object class
"""
class Card:
    """Class for the each Card object e.g. Ace of Hearts, King of Spades
    """
    number = 0
    name = ""
    type = ""
    played = False
    def __init__(self, name, number, ctype):
        self.number = number
        self.name = name
        self.type = ctype
