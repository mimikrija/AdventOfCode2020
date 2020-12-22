# --- Day 22: Crab Combat ---
from collections import deque

cards_input = open('inputs/22').read().split('\n\n')
both_decks = tuple(deque([int(card) for card in input_deck.split('\n')[1:]]) for input_deck in cards_input)

def get_score(deck):
    """returns the score `deck` score based on game rules"""
    # multiply every card value with their position counting
    # from the bottom of the deck
    return sum((len(deck)-n)*card for n, card in enumerate(deck))

def play_the_game(deck_1, deck_2):
    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()
        if card_1 > card_2:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)
    if len(deck_1) > 0:
        winner = deck_1
    else:
        winner = deck_2
    return winner
game = 0
def play_recursive_combat(deck_1, deck_2, game):
    round = 0
    game += 1
    configurations_1 = []
    configurations_2 = []
    # print(f'=== Game {game} ===')
    while len(deck_1) > 0 and len(deck_2) > 0:
        round += 1
        # print(f'-- Round {round} (Game {game}) --')
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
            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                # the winner of the round is determined by playing a new game of Recursive Combat
                # which is played by the remaining cards in their deck
                new_deck_1 = deque()
                for n, card in enumerate(deck_1):
                    if card_1 > n:
                        new_deck_1.append(card)
                new_deck_2 = deque()
                for n, card in enumerate(deck_2):
                    if card_2 > n:
                        new_deck_2.append(card)
                winner = play_recursive_combat(new_deck_1, new_deck_2, game)
                if winner == new_deck_1:
                    deck_1.append(card_1)
                    deck_1.append(card_2)
                else:
                    deck_2.append(card_2)
                    deck_2.append(card_1)
            else:
                # otherwise, the winner of the round is the player with the higher-value card
                if card_1 > card_2:
                    deck_1.append(card_1)
                    deck_1.append(card_2)
                    winner = deck_1
                    player = 'Player 1'
                else:
                    deck_2.append(card_2)
                    deck_2.append(card_1)
                    winner = deck_2
                    player = 'Player 2'
        # print(f"{player} wins round {round} of game {game}!\n")
    return winner



player_me, player_crab = both_decks
part_1 = get_score(play_the_game(player_me.copy(), player_crab.copy()))
print(f'The winning score after one game is {part_1}!')
# The winning score after one game is 32199!

player_me, player_crab = both_decks
part_2 = get_score(play_recursive_combat(player_me.copy(), player_crab.copy(), 0))
print(f'The winning score after >> RECURSIVE COMBAT CRAB vs ME << is {part_2}!')
# The winning score after >> RECURSIVE COMBAT CRAB vs ME << is 33780!
