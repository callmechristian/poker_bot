import numpy as np

class DealerHand:
    """Class object for the dealer hand

    Returns:
        cards: getCards() method returns dealer cards
    """
    cards = np.array([])
    deck = 0

    def __init__(self, cards, deck):
        self.cards = cards
        self.deck = deck
        self.sortCards()

    def addCard(self, card):
        """Adds the given card to the dealer stack

        Args:
            card (Card): Adds the card to the end of the stack
        """
        self.cards = np.append(self.cards, card)
        self.sortCards()

    def purge(self):
        """Remove all cards from the dealer
        """
        self.cards = np.array([])

    def setCards(self, cards):
        """Set dealer cards

        Args:
            cards (numpy array): Sets the dealer cards to the given numpy array of cards
        """
        self.cards = cards
        self.sortCards()

    def getCards(self):
        """Get cards that the dealer currently revealed

        Returns:
            np.array(cards): returns the numpy array with the revealed cards
        """
        return self.cards

    def sortCards(self):
        """Sort cards currently in dealer posession
        """
        for j in range (0, self.cards.size - 1):
            for i in range(0, self.cards.size - j - 1):
                if self.cards[i].nr > self.cards[i + 1].nr:
                    _t = self.cards[i]
                    self.cards[i] = self.cards[i+1]
                    self.cards[i+1] = _t
