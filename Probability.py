import numpy as np

class Probability:
    dealer_cards = np.array([])
    hand = np.array([])
    deck = np.array([])

    def __init__(self, deck, hand, dealer_cards):
        self.dealer_cards = dealer_cards
        self.deck = deck
        self.hand = hand

