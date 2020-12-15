starting_numbers = open('inputs/15').read().split(',')
starting_numbers = [int(num) for num in starting_numbers]

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
