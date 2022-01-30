import numpy as np

class WinningHand:
    name = ""
    priority = 0
    cards = np.array([])
    
    def __init__(self, name, priority, cards):
        self.name = name
        self.priority = priority
        self.cards = cards

    def getName(self):
        return self.name
    
    def getPriority(self):
        return self.priority
    
    def getCards(self):
        return self.cards
