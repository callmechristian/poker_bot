import numpy as np
from WinningHand import WinningHand
from Deck import Deck

# win_condition = {"Royal Flush": 10, "Straight Flush": 9, "Four of a Kind": 8, "Full House": 7, "Flush": 6, "Straight": 5, "Three of a Kind": 4, "Two Pair": 3, "One pair": 2, "High Card": 1}

class WinConditions:
    conditions = np.array([])
    def __init__(self, deck):
        # royal flush
        for i in range(0,3):
            condition_royal_flush = np.array([])
            for j in range(0,13):
                if j == 0 or j > 10:
                    condition_royal_flush = np.append(condition_royal_flush, deck.cards[(i+1)*j])
            self.conditions = np.append(self.conditions, WinningHand("Royal Flush", 10, condition_royal_flush))

        # straight flush
        for i in range(0,3):
            condition_straight_flush = np.array([])
            for j in range(0,13):
                for k in range(0,4):
                    condition_straight_flush = np.append(condition_straight_flush, deck.cards[(i+1)*j])
            self.conditions = np.append(self.conditions, WinningHand("Straight Flush", 9, condition_straight_flush))
        
        # four of a kind
        for i in range(0,3):
            condition_straight_flush = np.array([])
            for j in range(0,13):
                for k in range(0,4):
                    condition_straight_flush = np.append(condition_straight_flush, deck.cards[(i+1)*j])
            self.conditions = np.append(self.conditions, WinningHand("Straight Flush", 9, condition_straight_flush))