import numpy as np
from StackChecker import StackChecker

class CardStack:
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
        for j in range (0, self.cards.size - 1):
            for i in range(0, self.cards.size - j - 1):
                if self.cards[i].nr > self.cards[i + 1].nr:
                    _t = self.cards[i]
                    self.cards[i] = self.cards[i+1]
                    self.cards[i+1] = _t
    def print(self):
        print("Cards in stack: ")
        for card in self.cards:
            print(card.name)
    
    def checkHand(self):
        # check for hand values and card combinations
        # iterate over player and dealer cards
            if StackChecker.checkForRoyalFlush(self.cards):
                self.best_player_hand = "Royal Flush"
            elif StackChecker.checkForStraightFlush(self.cards):
                self.best_player_hand = "Straight Flush"
            elif StackChecker.checkForFourOfAKind(self.cards):
                self.best_player_hand = "Four of a Kind"
            elif StackChecker.checkForFullHouse(self.cards):
                self.best_player_hand = "Full House"
            elif StackChecker.checkForFlush(self.cards):
                self.best_player_hand = "Flush"
            elif StackChecker.checkForStraight(self.cards):
                self.best_player_hand = "Straight"
            elif StackChecker.checkForThreeOfAKind(self.cards):
                self.best_player_hand = "Three of a Kind"
            elif StackChecker.checkForTwoPair(self.cards):
                self.best_player_hand = "Two Pair"
            elif StackChecker.checkForOnePair(self.cards):
                self.best_player_hand = "One Pair"
            else:
                self.best_player_hand = "High Card"
        
            print("Best available hand: " + self.best_player_hand)
        

