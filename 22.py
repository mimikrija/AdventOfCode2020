# --- Day 22: Crab Combat ---
from collections import deque

cards_input = open('inputs/22').read().split('\n\n')
both_decks = tuple(deque([int(card) for card in input_deck.split('\n')[1:]]) for input_deck in cards_input)

def get_score(deck):
    """ returns the score `deck` score based on game rules """
    # multiply every card value with their position counting
    # from the bottom of the deck
    return sum((len(deck)-n)*card for n, card in enumerate(deck))

def play_round(in_deck_1, in_deck_2):
    deck_1 = in_deck_1.copy()
    deck_2 = in_deck_2.copy()

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
    return deck_1, deck_2


def play_the_game(deck_1, deck_2):
    """ returns `winner`, the winning deck after a standard game is
    played with `deck_1`, `deck_2` """

    # game is played as long as there are cards in both decks
    while deck_1 and deck_2:
        deck_1, deck_2 = play_round(deck_1, deck_2)

    # game over; determine who's the winner:
    for deck in (deck_1, deck_2):
        if deck:
            return deck


def play_recursive_combat(deck_1, deck_2):
    # round = 0
    configurations_1 = []
    configurations_2 = []
    # print(f'\n=== Game {game} ===')
    while len(deck_1) > 0 and len(deck_2) > 0:
        # round += 1
        # print(f'\n-- Round {round} (Game {game}) --')
        # print(f"Player 1's deck: {deck_1}")
        # print(f"Player 2's deck: {deck_2}")
        # check if the decks are in one of the previous configurations
        #print(configurations_1, configurations_2)
        if list(deck_1) in configurations_1 or list(deck_2) in configurations_2:
            winner = deck_1
            return winner
        else: # continue the game
            # append the decks to configurations
            configurations_1.append(list(deck_1))
            configurations_2.append(list(deck_2))

            # the players begin the round by each drawing the top card of their deck as normal
            card_1 = deck_1.popleft()
            card_2 = deck_2.popleft()

            # print(f'Player 1 plays: {card_1}')
            # print(f'Player 2 plays: {card_2}')

            # If both players have at least as many cards remaining in their deck
            # as the value of the card they just drew...
            if all(len(deck) >= card for deck, card in zip((deck_1, deck_2), (card_1, card_2))):
                # the winner of the round is determined by playing a new game of Recursive Combat
                # which is played by the remaining cards in their deck
                # print('Playing a sub-game to determine the winner...\n')
                new_deck_1 = deque()
                for n, card in enumerate(deck_1):
                    if card_1 > n:
                        new_deck_1.append(card)
                new_deck_2 = deque()
                for n, card in enumerate(deck_2):
                    if card_2 > n:
                        new_deck_2.append(card)
                winner = play_recursive_combat(new_deck_1, new_deck_2)
                # print(f'...anyway, back to game {parent_game}.')

                if winner == new_deck_1:
                    deck_1.append(card_1)
                    deck_1.append(card_2)
                    # player = 'Player 1'
                else:
                    deck_2.append(card_2)
                    deck_2.append(card_1)
                    # player = 'Player 2'
            else:
                # otherwise, the winner of the round is the player with the higher-value card
                if card_1 > card_2:
                    deck_1.append(card_1)
                    deck_1.append(card_2)
                    winner = deck_1
                    # player = 'Player 1'
                else:
                    deck_2.append(card_2)
                    deck_2.append(card_1)
                    winner = deck_2
                    # player = 'Player 2'
    #     print(f"{player} wins round {round} of game {game}!")
    # print(f'The winner of game {game} is {player}\n')
    return winner


player_me, player_crab = both_decks
part_1 = get_score(play_the_game(player_me.copy(), player_crab.copy()))
print(f'The winning score after one game is {part_1}!')
# The winning score after one game is 32199!

player_me, player_crab = both_decks
part_2 = get_score(play_recursive_combat(player_me.copy(), player_crab.copy()))
print(f'The winning score after >> RECURSIVE COMBAT CRAB vs ME << is {part_2}!')
# The winning score after >> RECURSIVE COMBAT CRAB vs ME << is 33780!
