# Day 15: Rambunctious Recitation

starting_numbers = open('inputs/15').read().split(',')
starting_numbers = [int(num) for num in starting_numbers]


def play_the_elves_game(selected_turns):
    rounds = max(selected_turns)

    # initialize dictionary of numbers with last two turns in the game they were said
    game_numbers = {num: (n + 1, n + 1) for n, num in enumerate(starting_numbers)}
    last_said_number = starting_numbers[-1]
    current_turn = len(game_numbers) + 1

    while current_turn <= rounds:
        # select the next number to be said
        say_next = game_numbers[last_said_number][1] - game_numbers[last_said_number][0]
        # update last two turns when the number was said
        if say_next in game_numbers.keys():
            next_to_last_turn, last_turn = game_numbers[say_next]
            last_two_turns = (last_turn, current_turn)
        else:
            last_two_turns = (current_turn, current_turn)
        # say the number!
        game_numbers[say_next] = last_two_turns
        last_said_number = say_next
        if current_turn in selected_turns:
             print(f'...after {current_turn} rounds is: {last_said_number}!')
        current_turn += 1
    return


turns_to_check = [2020, 30000000]
print('The result')
play_the_elves_game(turns_to_check)
# The result
# ...after 2020 rounds is: 1373!
# ...after 30000000 rounds is: 112458!
