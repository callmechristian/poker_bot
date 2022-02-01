"""Module to check for card combinations

Returns:
    Bool: checks the card combination and returns true if it matches
"""
import numpy as np

class StackChecker:
    """class for the checking functions
    """
    checked_hands = 0
    #TODO: use dict
    checked_royal_flush = 0
    checked_straight_flush = 0
    checked_four_of_a_kind = 0
    checked_full_house = 0
    checked_flush = 0
    checked_straight = 0
    checked_three_of_a_kind = 0
    checked_two_pair = 0
    checked_one_pair = 0

    def checkForRoyalFlush(self, cards):
        """checks for royal flush

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if royal flush present, false otherwise
        """
        self.checked_royal_flush += 1
        if cards[0].number%14 == 0:
            i = 9
            for card in cards:
                if card.number == i:
                    i = i + 1
            if i == 14:
                return True
        return False
    def checkForStraightFlush(self, cards):
        """checks for straight flush

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if straight flush present, false otherwise
        """
        self.checked_straight_flush += 1
        types = {"Hearts":0,"Spades":0,"Diamonds":0,"Clubs":0}
        for card in cards:
            for i in range(4):
                if card.type == list(types.keys())[i]:
                    types.update({card.type:(list(types.values())[i]+1)})

        for key, value in types.items():
            if value >= 5:
                prevnr = cards[0].number
                _ret = True
                # currently iterates through first card but doesn't need to.. fix?
                for card in cards:
                    if card.type == key:
                        if prevnr + 1 != card.number:
                            _ret = False
                        else:
                            prevnr = card.number
                return _ret
        return False
    def checkForFourOfAKind(self, cards):
        """checks for four of a kind

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if four of a kind present, false otherwise
        """
        self.checked_four_of_a_kind += 1
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                for k in range(j+1,cards.size):
                    for l in range (k+1, cards.size):
                        if l > cards.size:
                            continue
                        if (cards[i].number%13
                                == cards[j].number%13
                                == cards[k].number%13
                                == cards[l].number%13):
                            return True
        return False
    def checkForFullHouse(self, cards):
        """checks for full house

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if full house present, false otherwise
        """
        self.checked_full_house += 1
        three_of_a_kind_found = False
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                for k in range(j+1,cards.size):
                    if k > cards.size:
                        continue
                    if cards[i].number%13 == cards[j].number%13 == cards[k].number%13:
                        three_of_a_kind_found = True
                        cards = np.delete(cards, [i,j,k], None)
        if three_of_a_kind_found:
            if self.checkForOnePair(cards):
                return True
        return False
    def checkForFlush(self, cards):
        """checks for flush

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if flush present, false otherwise
        """
        self.checked_flush += 1
        types = {"Hearts":0,"Spades":0,"Diamonds":0,"Clubs":0}
        for card in cards:
            for i in range(4):
                if card.type == list(types.keys())[i]:
                    # check if at least 5 cards of this type have been found and exit if true
                    if list(types.values())[i]+1 >= 5:
                        return True
                    types.update({card.type:(list(types.values())[i]+1)})

        for value in list(types.values()):
            if value >= 5:
                return True
        return False
    def checkForStraight(self, cards):
        """checks for straight

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if straight present, false otherwise
        """
        self.checked_straight += 1
        prevnr = cards[0].number
        straightnrs = 0
        #TODO: currently iterates through first card but doesn't need to.. fix?
        for card in cards:
            if prevnr + 1 == card.number:
                straightnrs = straightnrs + 1
                prevnr = card.number
            if straightnrs >= 5:
                return True
        return False
    def checkForThreeOfAKind(self, cards):
        """checks for three of a kind

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if three of a kind present, false otherwise
        """
        self.checked_three_of_a_kind += 1
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                for k in range(j+1,cards.size):
                    if k > cards.size:
                        continue
                    if cards[i].number%13 == cards[j].number%13 == cards[k].number%13:
                        return True
        return False
    def checkForTwoPair(self, cards):
        """checks for two pair

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if two pair present, false otherwise
        """
        self.checked_two_pair += 1
        pairs = 0
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                if j > cards.size:
                    continue
                if cards[i].number%13 == cards[j].number%13:
                    pairs += 1
        if pairs >= 2:
            return True
        else:
            return False
    def checkForOnePair(self, cards):
        """checks for one pair

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if one pair present, false otherwise
        """
        self.checked_one_pair += 1
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                if j > cards.size:
                    continue
                if cards[i].number%13 == cards[j].number%13:
                    return True
        return False

    def checkHand(self, stack):
        """check for hand values and card combinations in given stack
        """
        self.checked_hands += 1
        if stack.cards.size > 0:
            if self.checkForRoyalFlush(stack.cards):
                stack.best_player_hand = "Royal Flush"
            elif self.checkForStraightFlush(stack.cards):
                stack.best_player_hand = "Straight Flush"
            elif self.checkForFourOfAKind(stack.cards):
                #TODO: return card number
                stack.best_player_hand = "Four of a Kind"
            elif self.checkForFullHouse(stack.cards):
                #TODO: return card numbers
                stack.best_player_hand = "Full House"
            elif self.checkForFlush(stack.cards):
                #TODO: return card type
                stack.best_player_hand = "Flush"
            elif self.checkForStraight(stack.cards):
                stack.best_player_hand = "Straight"
            elif self.checkForThreeOfAKind(stack.cards):
                #TODO: return card number
                stack.best_player_hand = "Three of a Kind"
            elif self.checkForTwoPair(stack.cards):
                #TODO: return card numbers
                stack.best_player_hand = "Two Pair"
            elif self.checkForOnePair(stack.cards):
                #TODO: return card number
                stack.best_player_hand = "One Pair"
            else:
                #TODO: return card number
                stack.best_player_hand = "High Card"
            print("Best available hand: " + stack.best_player_hand)
