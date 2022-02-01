import numpy as np
from Deck import Deck
from Hand import Hand
from DealerHand import DealerHand
from CardStack import CardStack
from StackChecker import StackChecker

d = Deck()

hand = Hand(np.array([d.cards[0],d.cards[7]]), d)
dealer = DealerHand(np.array([d.cards[11],d.cards[10],d.cards[9],d.cards[3],d.cards[8]]), d)

stack = CardStack(hand.cards, dealer.cards)
# stack.print()
checker = StackChecker()

# checker.checkHand(stack)


# print(d.cards[13].name)

# print("Player cards:")
# for card in hand.cards:
#     print(card.name)
# print("Dealer cards:")
# for card in dealer.cards:
#     print(card.name)