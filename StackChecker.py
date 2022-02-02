"""Module to check for card combinations

Returns:
    Bool: checks the card combination and returns true if it matches
"""
import numpy as np

class StackChecker:
    """class for the checking functions
    """
    # stats for this checker
    checked = {"hands": 0,
            "royals_flush": 0,
            "straight_flush":0,
            "four_of_a_kind":0,
            "full_house":0,
            "straight":0,
            "three_of_a_kind":0,
            "two_pair":0,
            "one_pair":0}

    def checkForRoyalFlush(self, cards):
        """checks for royal flush

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if royal flush present, false otherwise
        """
        self.checked["royal_flush"] += 1
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
        self.checked["straight_flush"] += 1
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
            dict: true if four of a kind present, false otherwise and the card number
        """
        self.checked["four_of_a_kind"] += 1
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
                            return {"four_of_a_kind": True, "card_number": cards[i].number%13}
        return {"four_of_a_kind": False}
    def checkForFullHouse(self, cards):
        """checks for full house

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if full house present, false otherwise
        """
        self.checked["full_house"] += 1
        three_of_a_kind_found = False
        three_pair = 0
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                for k in range(j+1,cards.size):
                    if k > cards.size:
                        continue
                    if cards[i].number%13 == cards[j].number%13 == cards[k].number%13:
                        three_pair = cards[i].number%13
                        three_of_a_kind_found = True
                        cards = np.delete(cards, [i,j,k], None)
        if three_of_a_kind_found:
            one_pair, one_pair_card = self.checkForOnePair(cards)
            if one_pair:
                return {"full_house": True, "three_pair": three_pair, "two_pair": one_pair_card}
        return {"full_house": False}
    def checkForFlush(self, cards):
        """checks for flush

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if flush present, false otherwise
        """
        self.checked["flush"] += 1
        types = {"Hearts":0,"Spades":0,"Diamonds":0,"Clubs":0}
        for card in cards:
            for i in range(4):
                if card.type == list(types.keys())[i]:
                    types.update({card.type:(list(types.values())[i]+1)})

        i = 0
        for value in list(types.values()):
            if value >= 5:
                return {"flush": True, "flush_type": list(types.keys())[i]}
            i += 1
        return {"flush": False}
    def checkForStraight(self, cards):
        """checks for straight

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if straight present, false otherwise
        """
        self.checked["straight"] += 1
        prevnr = cards[0].number
        straightnrs = 0
        #TODO: currently iterates through first card but doesn't need to.. fix?
        for card in cards:
            if prevnr + 1 == card.number:
                straightnrs = straightnrs + 1
                prevnr = card.number
            if straightnrs >= 5:
                return {"straight": False, "highest_card": prevnr}
        return {"straight": False}
    def checkForThreeOfAKind(self, cards):
        """checks for three of a kind

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if three of a kind present, false otherwise
        """
        self.checked["three_of_a_kind"] += 1
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                for k in range(j+1,cards.size):
                    if k > cards.size:
                        continue
                    if cards[i].number%13 == cards[j].number%13 == cards[k].number%13:
                        return {"three_of_a_kind": True, "card": cards[i].number%13}
        return {"three_of_a_kind": False}
    def checkForTwoPair(self, cards):
        """checks for two pair

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if two pair present, false otherwise
        """
        self.checked["two_pair"] += 1
        pairs = 0
        pairs_number = []
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                if j > cards.size:
                    continue
                if cards[i].number%13 == cards[j].number%13:
                    pairs_number.append(cards[i].number%13)
                    pairs += 1
        if pairs >= 2:
            # sort pairs by number
            highest_card = 0
            second_highest_card = 0
            if 0 in pairs_number:
                highest_card = 0
                for number in pairs_number:
                    if number > highest_card:
                        second_highest_card = number
            else:
                for number in pairs_number:
                    if number > highest_card:
                        second_highest_card = highest_card
                        highest_card = number
            return {"two_pair": True, "card1": highest_card,"card2": second_highest_card}
        else:
            return {"two_pair": False}
    def checkForOnePair(self, cards):
        """checks for one pair

        Args:
            cards (numpy array): numpy array of cards

        Returns:
            bool: true if one pair present, false otherwise
        """
        self.checked["one_pair"] += 1
        for i in range(cards.size):
            for j in range(i+1,cards.size):
                if j > cards.size:
                    continue
                if cards[i].number%13 == cards[j].number%13:
                    return {"one_pair": True, "card": cards[i].number%13}
        return {"one_pair": False}

    def checkHand(self, stack):
        """check for hand values and card combinations in given stack
        """
        self.checked["hands"] += 1
        if stack.cards.size > 0:
            if self.checkForRoyalFlush(stack.cards):
                stack.best_player_hand = "Royal Flush"
                return {"hand": "Royal Flush"}
            if self.checkForStraightFlush(stack.cards):
                stack.best_player_hand = "Straight Flush"
            four_of_a_kind, four_of_a_kind_card = self.checkForFourOfAKind(stack.cards)
            if four_of_a_kind:
                stack.best_player_hand = "Four of a Kind"
                return {"hand": "Royal Flush","card": four_of_a_kind_card}
            full_house, full_house_three_pair, full_house_two_pair = self.checkForFullHouse(stack.cards)
            if full_house:
                stack.best_player_hand = "Full House"
                return {"hand": "Full House", "three_pair": full_house_three_pair, "two_pair": full_house_two_pair}
            flush, flush_type, flush_highest = self.checkForFlush(stack.cards)
            if flush:
                stack.best_player_hand = "Flush"
                return {"hand": "Flush", "flush_type": flush_type, "highest_card": flush_highest}
            straight, straight_highest = self.checkForStraight(stack.cards)
            if straight:
                stack.best_player_hand = "Straight"
                return {"hand": "Straight", "highest_card": straight_highest}
            three_of_a_kind, three_of_a_kind_card = self.checkForThreeOfAKind(stack.cards)
            if three_of_a_kind:
                stack.best_player_hand = "Three of a Kind"
                return {"hand":"Three of a Kind", "card": three_of_a_kind_card}
            two_pair, two_pair_card1, two_pair_card2 = self.checkForTwoPair(stack.cards)
            if two_pair:
                stack.best_player_hand = "Two Pair"
                return {"hand":"Two Pair", "card1": two_pair_card1, "card2": two_pair_card2}
            one_pair, one_pair_card = self.checkForOnePair(stack.cards)
            if one_pair:
                stack.best_player_hand = "One Pair"
                return {"hand":"One Pair", "card": one_pair_card}
            stack.best_player_hand = "High Card"
            return {"hand":"High Card"}
        else:
            return {"hand": "No cards"}
