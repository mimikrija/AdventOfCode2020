
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

visited_positions = []

current_acc = 0
current_position = 0

while current_position not in visited_positions:
    if current_position == len(instructions):
        print('success')
        break
    visited_positions.append(current_position)
    action, argument = instructions[current_position]
    acc_offset, position_offset = do_stuff(action, argument)
    current_acc += acc_offset
    current_position += position_offset
print(current_acc) # 1553

for n, instruction in enumerate(instructions):
    action, argument = instruction
    if action == 'nop':
        new_action = 'jmp'
    if action == 'jmp':
        new_action = 'nop'
    new_instructions = list(instructions)
    new_instructions[n] = (new_action, argument)
    
    visited_positions = []

    current_acc = 0
    current_position = 0

    while current_position not in visited_positions:
        if current_position == len(new_instructions):
            print('success: ', current_acc)
            break
        visited_positions.append(current_position)
        action, argument = new_instructions[current_position]
        acc_offset, position_offset = do_stuff(action, argument)
        current_acc += acc_offset
        current_position += position_offset
    #print(current_acc, current_position, current_position == len(new_instructions)) # 1553
    if current_position == len(new_instructions):
        print(current_acc)
        break
# success:  1877 this one
# success:  505 not
# success:  895