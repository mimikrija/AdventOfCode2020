from collections import deque
starting_numbers = open('inputs/15').read().split(',')
starting_numbers = [int(num) for num in starting_numbers]


# part 2
# initialize dictionary of numbers with last two positions in the game
game_numbers = { num: (n + 1, n + 1) for n, num in enumerate(starting_numbers) }

last = starting_numbers[-1]
next_num = 0
turn = len(starting_numbers)+1

while turn <= 30000000:
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

    turn += 1
    
print(next_num) # 112458


last = starting_numbers[-1]
next_num = 0
turn = len(starting_numbers)+1

while turn <= 2020:
    if next_num in starting_numbers:
        search = list(reversed(starting_numbers))
        diff = turn - (len(search) - search.index(next_num) )
        starting_numbers.append(next_num)
        next_num = diff
    else:
        starting_numbers.append(next_num)
        next_num = 0
    turn += 1

print(starting_numbers[-1]) # 1373

