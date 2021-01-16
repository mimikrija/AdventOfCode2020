# Day 22: Crab Combat

from collections import deque

cards_input = open('inputs/22').read().split('\n\n')
both_decks = tuple(deque([int(card) for card in input_deck.split('\n')[1:]]) for input_deck in cards_input)

def get_score(deck):
    """ returns the score `deck` score based on game rules """
    # multiply every card value with their position counting
    # from the bottom of the deck
    return sum((len(deck)-n)*card for n, card in enumerate(deck))


def play_round(decks, condition):
    # move cards into the winning deck depending on the condition
    if condition:
        taker, loser = decks
    else:
        taker, loser = reversed(decks)
    # taker keeps their card and takes the loser's card
    taker.rotate(-1)
    taken_card = loser.popleft()
    taker.append(taken_card)
    return taker


def take_deck_part(in_deck):
    new_deck = deque()
    for n, card in enumerate(list(in_deck)[1:]):
        if in_deck[0] > n:
            new_deck.append(card)
    return new_deck


def play_combat_round(decks):
    # To play a sub-game of Recursive Combat, each player creates a new deck
    # by making a copy of the next cards in their deck
    # (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game)
    new_decks = tuple(take_deck_part(deck) for deck in decks)

    # the winner of the round is determined by playing a new game of Recursive Combat!
    sub_winner = play_recursive_combat(new_decks)
    winner = play_round(decks, sub_winner == new_decks[0])
    return winner

def play_the_game(decks):
    """ returns `winner`, the winning deck after a standard game is
    played with ``decks = (deck_1, `deck_2)` """

    # game is played as long as there are cards in both decks
    while all(deck for deck in decks):
        winner = play_round(decks, decks[0][0] > decks[1][0])

    # game over; determine who's the winner:
    return winner


def play_recursive_combat(decks):
    configurations_1 = []
    configurations_2 = []
    saved_configurations = (configurations_1, configurations_2)
 
    while all(deck for deck in decks):
        # if previous configuration met, player 1 wins
        if all(list(deck) in configurations for deck, configurations in zip(decks,saved_configurations)):
            return decks[0]
        
        # append saved configurations
        for deck, configurations in zip(decks, saved_configurations):
            configurations.append(list(deck))

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew...
        if all(len(deck)-1 >= deck[0] for deck in decks):
            # play combat round
            winner = play_combat_round(decks)
        else:
            # play one standard round (draw, two, larger wins)
            winner = play_round(decks, decks[0][0] > decks[1][0])

    return winner


players = tuple(deck.copy() for deck in both_decks)
part_1 = get_score(play_the_game(players))
print(f'The winning score after one game is {part_1}!')
# The winning score after one game is 32199!

players = tuple(deck.copy() for deck in both_decks)
part_2 = get_score(play_recursive_combat(players))
print(f'The winning score after >> RECURSIVE COMBAT CRAB vs ME << is {part_2}!')
# The winning score after >> RECURSIVE COMBAT CRAB vs ME << is 33780!
