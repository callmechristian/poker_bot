import numpy as np

class Hand:
    cards = np.array([])
    deck = 0
    
    def __init__(self, cards, deck):
        self.cards = cards
        self.deck = deck
        self.sortCards()

    def purge(self):
        self.cards = np.array([])
    
    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
        self.sortCards()

    def sortCards(self):
        for i in range(0,self.cards.size-1):
            if self.cards[i].nr > self.cards[i+1].nr:
                self.cards[[0,i]] = self.cards[[i,0]] # swap columns
    
