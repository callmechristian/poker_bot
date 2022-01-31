import numpy as np

class CardStack:
    cards = np.array([])
    hand = np.array([])
    dealer_hand = np.array([])
    winconditions = np.array([])

    def __init__(self, hand, dealerhand):
        self.hand = hand
        self.dealer_hand = dealerhand
        self
        self.cards = np.append(hand,dealerhand)
        self.sortCards()

    def sortCards(self):
        for i in range(0, self.cards.size - 1):
            if self.cards[i].nr > self.cards[i+1].nr:
                self.cards[[0,i]] = self.cards[[i,0]] # swap columns

    def checkHand(self):
        # check for hand values and card combinations
        pass
