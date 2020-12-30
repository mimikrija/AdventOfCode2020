from collections import Counter
import itertools

DELTAS = {dimension: set(itertools.product({-1,0,1}, repeat=dimension)) - {tuple(0 for _ in range(dimension))} for dimension in {3,4}}

# parse input into a set
with open('inputs/17') as inputfile:
    inputs = inputfile.readlines()
active_cubes_3D = {(row_num, column_num, 0)
                        for row_num, row in enumerate(inputs)
                        for column_num, column in enumerate(row.strip())
                        if column == '#'}

active_cubes_4D = {(row_num, column_num, 0, 0)
                        for row_num, row in enumerate(inputs)
                        for column_num, column in enumerate(row.strip())
                        if column == '#'}

def add_coordinates(tuple_1, tuple_2):
    return tuple(t_1 + t_2 for t_1, t_2 in zip(tuple_1,tuple_2))

def cube_neighbors(coordinate, dimension):
    return {add_coordinates(coordinate, delta) for delta in DELTAS[dimension]}

def conway_cycle(in_active_cubes, dimension):
    out_active_cubes = set()
    relevant_inactive_cubes = set()
    for cube in in_active_cubes:
        relevant_inactive_cubes |= {neighbor for neighbor in cube_neighbors(cube, dimension) if neighbor not in in_active_cubes}

    for cube in in_active_cubes | relevant_inactive_cubes:
        neighbors = cube_neighbors(cube, dimension)
        count_active_neighbors = sum(neighbor in in_active_cubes for neighbor in neighbors)
        if (cube in in_active_cubes and count_active_neighbors in {2,3}) or (cube in relevant_inactive_cubes and count_active_neighbors == 3):
            out_active_cubes.add(cube)

    return out_active_cubes

cycles = 6

for _ in range(cycles):
    active_cubes_3D = conway_cycle(active_cubes_3D, 3)
    active_cubes_4D = conway_cycle(active_cubes_4D, 4)
party_1 = len(active_cubes_3D)
party_2 = len(active_cubes_4D)

print(f'The number of active 3D cubes after {cycles} cycles is {party_1}!')
# The number of active cubes after 6 cycles is 346!

print(f'The number of active 4D cubes after {cycles} cycles is {party_2}!')
# The number of active cubes after 6 cycles is 1632!
