from collections import Counter

def count_neighbors(cube, positions):
    x, y, z = cube
    counter = 0
    for delta_x in {-1, 0, 1}:
         for delta_y in {-1, 0, 1}:
              for delta_z in {-1, 0, 1}:
                    if delta_x == delta_y == delta_z == 0:
                        continue
                    else:
                        counter += positions.get((x+delta_x, y+delta_y, z+delta_z), '.') == '#'
    return counter

def generate_neighbors(cube, in_positions):
    known_positions = set(in_positions.keys())
    x, y, z = cube
    new_neighbors = set()
    for delta_x in {-1, 0, 1}:
         for delta_y in {-1, 0, 1}:
              for delta_z in {-1, 0, 1}:
                    new_cube = (x+delta_x, y+delta_y, z+delta_z)
                    if delta_x == delta_y == delta_z == 0:
                        continue
                    else:
                        new_neighbors.add(new_cube)
    return new_neighbors - known_positions

def widen_the_map(in_positions):
    positions = in_positions.copy()
    all_neighbors = set()
    for cube in in_positions:
        all_neighbors = all_neighbors.union(generate_neighbors(cube, in_positions))
    for new_neighbor in all_neighbors:
        positions[new_neighbor] = '.'
    return positions

def de_acitivation(in_positions):
    positions = in_positions.copy()
    for cube in in_positions:
        # active becomes inactive
        if in_positions.get(cube, '.') == '#' and count_neighbors(cube, in_positions) not in {2, 3}:
            positions[cube] = '.'
        # inactive becomes active
        else:
            if in_positions.get(cube, '.') == '.' and count_neighbors(cube, in_positions) == 3:
                positions[cube] = '#'
    return positions

with open('inputs/17') as inputfile:
    inputs = inputfile.readlines()

# parse input into a dictionary of cube coordinates (z is initialized to 0)
initial_configuration = {(row_num, column_num, 0): column
                        for row_num, row in enumerate(inputs)
                        for column_num, column in enumerate(row.strip())
                        }

previous_configuration = initial_configuration.copy()

for _ in range (6):
    current_configuration = widen_the_map(previous_configuration)
    current_configuration = de_acitivation(current_configuration)
    previous_configuration = current_configuration.copy()

part_1 = Counter(current_configuration.values())['#']
print(f'Number of active cells after 6 cycles is: {part_1}!')
# Number of active cells after 6 cycles is: 346!


def count_neighbors(cube, positions):
    x, y, z, w  = cube
    counter = 0
    for delta_x in {-1, 0, 1}:
         for delta_y in {-1, 0, 1}:
              for delta_z in {-1, 0, 1}:
                  for delta_w in {-1, 0, 1}:
                        if delta_x == delta_y == delta_z == delta_w == 0:
                            continue
                        else:
                            counter += positions.get((x+delta_x, y+delta_y, z+delta_z, w+delta_w), '.') == '#'
    return counter

def generate_neighbors(cube, in_positions):
    known_positions = set(in_positions.keys())
    x, y, z, w = cube
    new_neighbors = set()
    for delta_x in {-1, 0, 1}:
         for delta_y in {-1, 0, 1}:
              for delta_z in {-1, 0, 1}:
                   for delta_w in {-1, 0, 1}:
                        new_cube = (x+delta_x, y+delta_y, z+delta_z, w+delta_w)
                        if delta_x == delta_y == delta_z == delta_w == 0:
                                continue
                        else:
                            new_neighbors.add(new_cube)
    return new_neighbors - known_positions

def widen_the_map(in_positions):
    positions = in_positions.copy()
    all_neighbors = set()
    for cube in in_positions:
        all_neighbors = all_neighbors.union(generate_neighbors(cube, in_positions))
    for new_neighbor in all_neighbors:
        positions[new_neighbor] = '.'
    return positions

def de_acitivation(in_positions):
    positions = in_positions.copy()
    for cube in in_positions:
        # active becomes inactive
        if in_positions.get(cube, '.') == '#' and count_neighbors(cube, in_positions) not in {2, 3}:
            positions[cube] = '.'
        # inactive becomes active
        else:
            if in_positions.get(cube, '.') == '.' and count_neighbors(cube, in_positions) == 3:
                positions[cube] = '#'
    return positions

with open('inputs/17') as inputfile:
    inputs = inputfile.readlines()

# parse input into a dictionary of cube coordinates (z is initialized to 0)
initial_configuration = {(row_num, column_num, 0, 0): column
                        for row_num, row in enumerate(inputs)
                        for column_num, column in enumerate(row.strip())
                        }
#print(initial_configuration)
previous_configuration = initial_configuration.copy()
import time
for n in range (6):
    start = time.time()
    current_configuration = widen_the_map(previous_configuration)
    current_configuration = de_acitivation(current_configuration)
    previous_configuration = current_configuration.copy()
    part_2 = Counter(current_configuration.values())['#']
    end = time.time()
    print(f'Number of active cells after {n+1} cycles is: {part_1} Time needed = {1000*(end-start)}!')

# Number of active cells after 1 cycles is: 170 Time needed = 31.981468200683594!
# Number of active cells after 2 cycles is: 174 Time needed = 320.8167552947998!
# Number of active cells after 3 cycles is: 816 Time needed = 2351.656436920166!
# Number of active cells after 4 cycles is: 508 Time needed = 14296.834707260132!
# Number of active cells after 5 cycles is: 2100 Time needed = 104869.29035186768!
# Number of active cells after 6 cycles is: 1632 Time needed = 285671.8304157257!
