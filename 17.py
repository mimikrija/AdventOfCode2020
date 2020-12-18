from collections import Counter
import itertools
dimension = 3
deltas = set(itertools.product({-1,0,1}, repeat=dimension))

with open('inputs/17-ex') as inputfile:
    inputs = inputfile.readlines()
# parse input into a set
active_cubes = set((row_num, column_num, 0)
                        for row_num, row in enumerate(inputs)
                        for column_num, column in enumerate(row.strip())
                        if column == '#')
dim_x = len(inputs[0].strip())
dim_y = len(inputs)
flat_dim = max(dim_x, dim_y)

# domain = itertools.product(range(-flat_dim*6,flat_dim*6+1), repeat = dimension)
# domain_purged_3d = (di for di in domain if di[2] in range(-6, 7))

def add_coordinates(tuple_1, tuple_2):
    return tuple(t_1 + t_2 for t_1, t_2 in zip(tuple_1,tuple_2))

def count_neighbors(cube, positions):
    out_positions = positions.copy()
    counter = 0
    neighbors = []
    for delta in deltas:
        if delta == (0, 0, 0):
            continue
        neighbor = add_coordinates(cube, delta)
        neighbors.append(neighbor)
        counter += neighbor in positions
    if counter not in {2, 3}:
        positions.remove(cube)
    # check neighbors, add  if it needs to be activated
    return #return out_positions counter

#print(count_neighbors((1,2,0),active_cubes))

