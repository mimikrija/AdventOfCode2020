# --- Day 22: Crab Combat ---
from collections import deque

cards_input = open('inputs/22').read().split('\n\n')


player_me = deque()
player_crab = deque()

for n, deck in enumerate(cards_input):
    deck = deck.split('\n')
    for card in deck[1:]:
        if n == 0:
            player_me.append(int(card))
        else:
            player_crab.append(int(card))

