from collections import deque
starting_numbers = open('inputs/15').read().split(',')
starting_numbers = [int(num) for num in starting_numbers]


def play_the_elves_game(selected):
    # initialize dictionary of numbers with last two positions in the game
    rounds = max(selected)
    game_numbers = {num: (n + 1, n + 1) for n, num in enumerate(starting_numbers)}
    next_num = 0
    turn = len(game_numbers) + 1
    while turn <= rounds:
        if next_num in game_numbers.keys():
            positions = game_numbers[next_num]
            diff = positions[1] - positions[0]
        else:
            diff = 0
        if diff in game_numbers.keys():
            last = game_numbers[diff][1]
        else:
            last = turn
        game_numbers[diff] = ( last ,turn)
        next_num = diff
        if turn in selected:
             print(f'...after {turn} rounds is: {next_num}!')
        turn += 1
    return


turns_to_check = [2020, 30000000]
print('The result')
play_the_elves_game(turns_to_check)
# The result
# ...after 2020 rounds is: 1373!
# ...after 30000000 rounds is: 112458!
