# Day 8: Handheld Halting

with open('inputs/08') as inputfile:
    inputs = inputfile.readlines()

instructions = [(line.strip().split()[0], int(line.strip().split()[1])) for line in inputs]

def do_stuff(action, argument):
    if action == 'nop':
        return 0, 1
    if action == 'acc':
        return argument, 1
    if action == 'jmp':
        return 0, argument

def run_program(instructions):
    visited_positions = []

    current_acc = 0
    current_position = 0

    while current_position not in visited_positions:
        if current_position == len(instructions):
            break
        visited_positions.append(current_position)
        action, argument = instructions[current_position]
        acc_offset, position_offset = do_stuff(action, argument)
        current_acc += acc_offset
        current_position += position_offset
    return(current_acc, current_position)

print(f'Part 1 solution is: {run_program(instructions)[0]}!')
# Part 1 solution is: 1553!

for n, instruction in enumerate(instructions):
    action, argument = instruction
    if action == 'nop':
        new_action = 'jmp'
    if action == 'jmp':
        new_action = 'nop'
    new_instructions = list(instructions)
    new_instructions[n] = (new_action, argument)
    current_acc, current_position = run_program(new_instructions)
    if current_position == len(new_instructions):
        print(f'Part 2 solution is: {current_acc}!')
        break
# Part 2 solution is: 1877!
