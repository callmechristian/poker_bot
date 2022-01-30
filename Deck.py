import numpy as np
from Card import Card

class Deck:
    cards = np.array([])
    type_stack = np.array(["Hearts", "Spades", "Clubs", "Diamonds"])
    def __init__(self):
        i = 0
        j = 0
        while i < 4:
            while j < 14:
                if 1 < j <11:
                    self.cards = np.append(self.cards, (i+1)*j, Card(str(j),self.type_stack[i]))
                elif j == 0:
                    self.cards = np.append(self.cards, (i+1)*j, Card("Ace",self.type_stack[i]))
                elif j == 11:
                    self.cards = np.append(self.cards, (i+1)*j, Card("Jack",self.type_stack[i]))
                elif j == 12:
                    self.cards = np.append(self.cards, (i+1)*j, Card("Queen",self.type_stack[i]))
                elif j == 13:
                    self.cards = np.append(self.cards, (i+1)*j, Card("King",self.type_stack[i]))
                j = j + 1
            i = i + 1
            j = 0
