import re
from collections import Counter
from itertools import combinations

def to_binary(num):
    num_bin = "{0:036b}".format(num)
    return num_bin

def apply_bitmask(mask, memory_value):
    memory_bin =  to_binary(memory_value)
    for n, c in enumerate(mask):
        if c != 'X':
            memory_bin = memory_bin[:n] + c + memory_bin[n+1:]
    return int(memory_bin, 2)

def get_floating(mask, memory_ad):
    """ generates a memory address with X's """
    memory_with_X = to_binary(int(memory_ad))
    base_memory = to_binary(int(memory_ad))
    for n, c in enumerate(mask):
        if c != '0':
            memory_with_X = memory_with_X[:n] + c + memory_with_X[n+1:]
    for n, c in enumerate(mask):
        if c == 'X':
            base_memory = base_memory[:n] + '0' + base_memory[n+1:]
        if c == '1':
            base_memory = base_memory[:n] + '1' + base_memory[n+1:]
    return(memory_with_X, int(base_memory,2))

def generate_adresses(base_address, memory_floating):
    """returns a list of address keys where a value should be written"""
    addresses_additions = [0]
    all_additions = [ 2**(35-n) for n, c in enumerate(memory_floating) if c == 'X' ]
    # generate all combinations of values to add based on the bitmask
    for n in range (1, len(all_additions)+1):
        addresses_additions += [sum([num for num in combo]) for combo in combinations(all_additions,n)]
    # generate a list of keys for memory values
    address_list = [str(base_address + add) for add in addresses_additions]
    return(address_list)


inputs = open('inputs/14').read().split('mask = ')
inputs = inputs[1:]

program_instructions = []

# parse program instructions into [mask, [list of memory stuff]]
# list of memory stuff has the first location as a string (we'll use that
# as program_memory keys, and the second is converted to int because these
# are the values we'll be adding later)
digits = re.compile(r'[0-9]+')
for chunk in inputs:
    chunk = chunk.split('\n')
    memory_stuff = [re.findall(digits,mem) for mem in chunk[1:] if mem!= '']
    for n, memory_data in enumerate(memory_stuff):
        memory_data[1] = int(memory_data[1])
    program_instructions.append([chunk[0], memory_stuff])


# initialize empty memories
program_memory_1 = {}
program_memory_2 = {}

# run the instructions to fill the memories
for mask, memory_stuff in program_instructions:
    for memory_address, value in memory_stuff:
        # part 2: fill a single memory slot with whatever value we get after applying the bitmask
        program_memory_1[memory_address] = apply_bitmask(mask, value)
        # part 2: fill a generated list of memory locations with value
        floating, base = get_floating(mask, memory_address)
        memory_locations = generate_adresses(base, floating)
        for location in memory_locations:
            program_memory_2[location] = value

part_1 = sum(program_memory_1.values())
part_2 = sum(program_memory_2.values())

print(f'The sum of all values in memory after the program completes is {part_1}!' )
print(f'The sum of all values in memory after the program completes is, part 2 is: {part_2}!' )
# The sum of all values in memory after the program completes is 13727901897109!
# The sum of all values in memory after the program completes is, part 2 is: 5579916171823!
