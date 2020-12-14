def to_binary(num):
    num_bin = "{0:036b}".format(num)
    return num_bin

def apply_bitmap(memory_dict, mask, memory_location, memory_value):
    memory_bin =  to_binary(memory_value)
    for n, c in enumerate(mask):
        if c != 'X':
            memory_bin = memory_bin[:n] + c + memory_bin[n+1:]
    memory_dict[memory_location] = memory_bin


# read data in bulks
inputs = open('inputs/14').read().split('mask = ')
inputs = inputs[1:]

program_memory = {}

for chunk in inputs:
    chunk = chunk.split('\n')
    for n, line in enumerate(chunk):
        if line == '':
            continue
        if n == 0:
            mask = line
        else:
            memory, to_write = line.split(' = ')
            to_write = int(to_write)
            apply_bitmap(program_memory, mask, memory, to_write)

part_1 = sum([int(memory,2) for memory in program_memory.values()])

print(part_1) # 13727901897109
