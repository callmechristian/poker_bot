"""The available known cards to check for combinations and probabilities
"""

import numpy as np

class CardStack:
    """The class object for available cards
    """
    cards = np.array([])
    hand = np.array([])
    dealer_hand = np.array([])

    best_player_hand = "High Card"

    def __init__(self, hand, dealerhand):
        self.hand = hand
        self.dealer_hand = dealerhand
        self.best_player_hand = "High Card"
        self.cards = np.append(hand,dealerhand)
        self.sortCards()

    def sortCards(self):
        """Sort the cards in the stack
        """
        for j in range (0, self.cards.size - 1):
            for i in range(0, self.cards.size - j - 1):
                if self.cards[i].number > self.cards[i + 1].number:
                    _t = self.cards[i]
                    self.cards[i] = self.cards[i+1]
                    self.cards[i+1] = _t
    def print(self):
        """print cards in stack
        """
        print("Cards in stack: ")
        for card in self.cards:
            print(card.name)
