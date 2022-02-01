"""module to determine various probabilities
"""
import numpy as np

class Probability:
    """object class wrapper for probability calculators
    """
    dealer_cards = np.array([])
    hand = np.array([])
    deck = np.array([])
    stack = np.array([])
    remaining_cards = np.array([])
    remaining_types = {"Hearts": 13, "Spades": 13, "Diamonds": 13, "Clubs": 13}
    win_chance = 0

    def __init__(self, deck, hand, dealer_cards, stack):
        self.dealer_cards = dealer_cards
        self.deck = deck
        self.hand = hand
        self.stack = stack
        cond = []
        for card in dealer_cards:
            if card.type in list(self.remaining_types.keys()):
                self.remaining_types[card.type] -= 1
            cond.append(card.number)
        for card in hand:
            if card.type in list(self.remaining_types.keys()):
                self.remaining_types[card.type] -= 1
            cond.append(card.number)
        self.remaining_cards = np.delete(deck, cond)

    def predictNextCardType(self):
        """predicts the next card type based on remaining cards
        """
        # honestly pretty useless since cards are random
        p_hearts = self.remaining_types["Hearts"]/self.remaining_cards.size
        p_clubs = self.remaining_types["Clubs"]/self.remaining_cards.size
        p_diamonds = self.remaining_types["Diamonds"]/self.remaining_cards.size
        p_spades = self.remaining_types["Spades"]/self.remaining_cards.size

        if self.dealer_cards.size <= 3:
            print("Next card type probability:",
            "\nHearts ",p_hearts,
            "% \nSpades ",p_spades,
            "% \nDiamonds ",p_diamonds,
            "% \nClubs ",p_clubs,"%")
        else:
            print("Cards are already final")

    def predictWinChance(self):
        """predicts win chance with current cards based on remaining cards
        """
        if self.stack.best_player_hand == "Royal Flush":
            self.win_chance = 100
        if self.stack.best_player_hand == "Straight Flush":
            types = {"Hearts":0,"Spades":0,"Diamonds":0,"Clubs":0}
            flush_type = ""
            for card in self.stack.cards:
                for i in range(4):
                    if card.type == list(types.keys())[i]:
                        types.update({card.type:(list(types.values())[i]+1)})
            typenr = max(list(types.values()))
            for key, value in types.items():
                if typenr == value:
                    flush_type = key
                    continue
            for card in self.hand.cards:
                if card.type == flush_type:
                    if card.number == 0:
                        self.win_chance = 100
                    else:
                        # win chance based on highest card in players hand that is same type as flush
                        self.win_chance = (13-card.number/13)*100
        if self.stack.best_player_hand == "Four of a Kind":
            #TODO: implement after updating stackchecker
            pass
            