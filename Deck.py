import numpy as np
from Card import Card

class Deck:
    cards = np.array([])
    type_stack = np.array(["Hearts", "Spades", "Clubs", "Diamonds"])
    def __init__(self):
        for i in range(0,4):
            for j in range(0,14):
                if j == 0:
                    self.cards = np.append(self.cards, Card("Ace of " + self.type_stack[i], (i+1)*j, self.type_stack[i]))
                elif 1 < j <11:
                    self.cards = np.append(self.cards, Card(str(j) + " of " + self.type_stack[i] , (i+1)*j, self.type_stack[i]))
                elif j == 11:
                    self.cards = np.append(self.cards, Card("Jack of " + self.type_stack[i], (i+1)*j, self.type_stack[i]))
                elif j == 12:
                    self.cards = np.append(self.cards, Card("Queen of " + self.type_stack[i], (i+1)*j, self.type_stack[i]))
                elif j == 13:
                    self.cards = np.append(self.cards, Card("King of " + self.type_stack[i], (i+1)*j, self.type_stack[i]))
