class StackChecker:
    def checkForRoyalFlush(cards):
        # print(cards[0].nr)
        if cards[0].nr%14 == 0:
            i = 9
            for card in cards:
                if card.nr == i:
                    i = i + 1
            if i == 14:
                return True
        return False
    def checkForStraightFlush(cards):
        return False
    def checkForFourOfAKind(cards):
        return False
    def checkForFullHouse(cards):
        return False
    def checkForFlush(cards):
        return False
    def checkForStraight(cards):
        return False
    def checkForThreeOfAKind(cards):
        return False
    def checkForTwoPair(cards):
        return False
    def checkForOnePair(cards):
        return False