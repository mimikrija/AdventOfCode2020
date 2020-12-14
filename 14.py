from collections import Counter
from itertools import combinations

def to_binary(num):
    num_bin = "{0:036b}".format(num)
    return num_bin

def apply_bitmask(memory_dict, mask, memory_location, memory_value):
    memory_bin =  to_binary(memory_value)
    for n, c in enumerate(mask):
        if c != 'X':
            memory_bin = memory_bin[:n] + c + memory_bin[n+1:]
    memory_dict[memory_location] = memory_bin

def get_floating(mask, memory_ad):
    """ generates a memory address with X's """
    memory_with_X = to_binary(memory_ad)
    base_memory = to_binary(memory_ad)
    for n, c in enumerate(mask):
        if c != '0':
            memory_with_X = memory_with_X[:n] + c + memory_with_X[n+1:]
    for n, c in enumerate(mask):
        if c == 'X':
            base_memory = base_memory[:n] + '0' + base_memory[n+1:]
        if c == '1':
            base_memory = base_memory[:n] + '1' + base_memory[n+1:]
    return(memory_with_X, int(base_memory,2))
import re
digits = re.compile(r'[0-9]+')
def generate_adresses(base_address, memory_floating):
    """returns a list of address keys where a value should be written"""
    addresses_additions = [0]
    all_additions = [ 2**(35-n) for n, c in enumerate(memory_floating) if c == 'X' ]
    # generate all combinations of values to add
    for n in range (1, len(all_additions)+1):
        addresses_additions += [sum([num for num in combo]) for combo in combinations(all_additions,n)]
    # generate a list of keys for memory values
    address_list = [ 'mem[' + str( base_address + add) + ']' for add in addresses_additions]
    return(address_list)

def write_to_memories(memory_dict, mask, memory_location, memory_value):
    memory_loc = int(re.findall(digits,memory_location)[0])
    floating, base = get_floating(mask,memory_loc)
    memory_locations = generate_adresses(base, floating)
    for location in memory_locations:
        memory_dict[location] = memory_value


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
            apply_bitmask(program_memory, mask, memory, to_write)

part_1 = sum([int(memory,2) for memory in program_memory.values()])

print(part_1) # 13727901897109


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
            write_to_memories(program_memory, mask, memory, to_write)

part_2 = sum([memory for memory in program_memory.values()])
print(part_2) # 5579916171823


