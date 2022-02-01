"""Module for the hand object

Returns:
    np.array(cards): getCards() returns the numpy array of cards currently in the stack
"""
import numpy as np

class Hand:
    """Object class for the player hand stack

    Returns:
        np.array(cards): returns the numpy array of cards currently in the players hand
    """
    cards = np.array([])
    deck = 0

    def __init__(self, cards, deck):
        self.cards = cards
        self.deck = deck
        self.sortCards()

    def purge(self):
        """clear player hand
        """
        self.cards = np.array([])

    def getCards(self):
        """Return the cards currently in the players hand

        Returns:
            np.array(cards): the numpy array of player cards
        """
        return self.cards

    def setCards(self, cards):
        """Set the cards in the players hand

        Args:
            cards (numpy array): the numpy array to be set as players cards
        """
        self.cards = cards
        self.sortCards()

    def sortCards(self):
        """Sort the cards in the players hand
        """
        for j in range (0, self.cards.size - 1):
            for i in range(0, self.cards.size - j - 1):
                if self.cards[i].nr > self.cards[i + 1].nr:
                    _t = self.cards[i]
                    self.cards[i] = self.cards[i+1]
                    self.cards[i+1] = _t
    
