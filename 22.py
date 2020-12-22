# --- Day 22: Crab Combat ---
from collections import deque

cards_input = open('inputs/22').read().split('\n\n')
both_decks = tuple(deque([int(card) for card in input_deck.split('\n')[1:]]) for input_deck in cards_input)

def get_score(deck):
    """ returns the score `deck` score based on game rules """
    # multiply every card value with their position counting
    # from the bottom of the deck
    return sum((len(deck)-n)*card for n, card in enumerate(deck))

def play_round(deck_1, deck_2):

    if deck_1[0] > deck_2[0]:
        taker = deck_1
        loser = deck_2
    else:
        taker = deck_2
        loser = deck_1
    # taker keeps their card and takes the loser's card
    taker.rotate(-1)
    taken_card = loser.popleft()
    taker.append(taken_card)

    # we must return them in the correct order, regardless of
    # who the winner is
    return deck_1, deck_2, taker

def play_combat_round(deck_1, deck_2):
    card_1 = deck_1.popleft()
    card_2 = deck_2.popleft()
    # To play a sub-game of Recursive Combat, each player creates a new deck
    # by making a copy of the next cards in their deck
    # (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game)
    new_deck_1 = deque()
    for n, card in enumerate(deck_1):
        if card_1 > n:
            new_deck_1.append(card)
    new_deck_2 = deque()
    for n, card in enumerate(deck_2):
        if card_2 > n:
            new_deck_2.append(card)
    
    # the winner of the round is determined by playing a new game of Recursive Combat!
    new_deck_1, new_deck_2, sub_winner = play_recursive_combat(new_deck_1, new_deck_2)
    if sub_winner == new_deck_1:
        deck_1.append(card_1)
        deck_1.append(card_2)
        winner = deck_1
    else:
        deck_2.append(card_2)
        deck_2.append(card_1)
        winner = deck_2
    return deck_1, deck_2, winner

def play_the_game(deck_1, deck_2):
    """ returns `winner`, the winning deck after a standard game is
    played with `deck_1`, `deck_2` """

    # game is played as long as there are cards in both decks
    while deck_1 and deck_2:
        deck_1, deck_2, winner = play_round(deck_1, deck_2)

    # game over; determine who's the winner:
    return winner


def play_recursive_combat(deck_1, deck_2):

    configurations_1 = []
    configurations_2 = []

    while deck_1 and deck_2:
        # first check if the decks are in one of the previously seen configurations
        # and end the game if yes
        if list(deck_1) in configurations_1 or list(deck_2) in configurations_2:
            winner = deck_1
            return deck_1, deck_2, winner

        # continue the game
        # append the decks to configurations
        configurations_1.append(list(deck_1))
        configurations_2.append(list(deck_2))

        # the players begin the round by each drawing the top card of their deck as normal

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew...
        if all(len(deck)-1 >= deck[0] for deck in (deck_1, deck_2)):
            # play combat round
            deck_1, deck_2, winner = play_combat_round(deck_1, deck_2)
        else:
            # play one standard round (draw, two, larger wins)
            deck_1, deck_2, winner = play_round(deck_1, deck_2)

    return deck_1, deck_2, winner


player_me, player_crab = both_decks
part_1 = get_score(play_the_game(player_me.copy(), player_crab.copy()))
print(f'The winning score after one game is {part_1}!')
# The winning score after one game is 32199!

player_me, player_crab = both_decks
part_2 = get_score(play_recursive_combat(player_me.copy(), player_crab.copy())[2])
print(f'The winning score after >> RECURSIVE COMBAT CRAB vs ME << is {part_2}!')
# The winning score after >> RECURSIVE COMBAT CRAB vs ME << is 33780!
