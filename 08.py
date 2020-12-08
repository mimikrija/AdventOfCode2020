
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
    visited_positions.append(current_position)
    action, argument = instructions[current_position]
    acc_offset, position_offset = do_stuff(action, argument)
    current_acc += acc_offset
    current_position += position_offset
print(current_acc) # 1553
