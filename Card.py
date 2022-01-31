class Card:
    nr = 0
    name = ""
    type = ""
    played = False
    def __init__(self, name, nr, type):
        self.nr = nr
        self.name = name
        self.type = type