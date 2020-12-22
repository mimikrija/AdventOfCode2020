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

def play_the_game(player_1, player_2):
    while len(player_1) > 0 and len(player_2) > 0:
        card_1 = player_1.popleft()
        card_2 = player_2.popleft()
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    if len(player_1) > 0:
        winner = player_1
    else:
        winner = player_2
    result = sum((len(winner)-n) * card for n, card in enumerate(winner))
    return result


part_1 = play_the_game(player_me, player_crab)
print(part_1) # 32199
