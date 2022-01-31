import numpy as np
from Deck import Deck
from Hand import Hand
from DealerHand import DealerHand
from CardStack import CardStack

d = Deck()

hand = Hand(np.array([d.cards[0],d.cards[14]]), d)
dealer = DealerHand(np.array([d.cards[1],d.cards[2],d.cards[4],d.cards[3],d.cards[8]]), d)

stack = CardStack(hand.cards, dealer.cards)

# print("Player cards:")
# for card in hand.cards:
#     print(card.name)
# print("Dealer cards:")
# for card in dealer.cards:
#     print(card.name)