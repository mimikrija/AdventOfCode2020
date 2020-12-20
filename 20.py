import re
from collections import Counter
from itertools import product
# every tile is a dict ID: [side_N, side_E, side_S, side_W]
# I still need to think of a nice convention of writing slide nums
# every tile was rotated and flipped - this means that we don't know the order of N, E, S, W,
# but we do know that two sides are flipped, either N to S or E to W
# in that sense every tile has two possible configurations (we'll worry about rotation later)

# each tile has 10 bits
TILE_SIZE = 10 # input array len

def convert_sides_to_num(in_sides):
    return [int(side,2) for side in in_sides]

    # for side in in_sides:
    #     binary = in_string.translate(str.maketrans('#.','10'))
    # return int(binary, 2)

def generate_configurations(in_sides):
    # there are 4 possible configurations: original/rotated, flipped horizontally, flipped vertically, fliped both
    # this is fishy but works for now
    flipped_v = [] # flipped vertically N-S
    flipped_h = [] # flipped vertically E-W
    flipped_both = []
    for n, side in enumerate(in_sides):
        if n % 2 == 0:
            flipped_v.append(''.join(reversed(side)))
            flipped_h.append(side)
        else:
            flipped_v.append(side)
            flipped_h.append(''.join(reversed(side)))
    temp1 = flipped_v[1]
    temp2 = flipped_v[3]
    flipped_v[3] = temp1
    flipped_v[1] = temp2
    temp1 = flipped_h[0]
    temp2 = flipped_h[2]
    flipped_h[2] = temp1
    flipped_h[0] = temp2
    return [in_sides, flipped_v, flipped_h]

re_numbers = re.compile(r'\d+')
inputs = open('inputs/20-ex').read().split('\n\n')
input_tiles = {}
TILE_SIZE = 10 # ovo izracunaj!
NUMBER_OF_TILES = len(inputs)

for tile in inputs:
    tile_data = tile.split('\n')
    ID = re.findall(re_numbers, tile_data[0])[0]
    tile_rows = tile_data[1:]
    #tile_array = [row for row in tile_rows]
    #tile_array = [ convert_side_to_num(row) for row in tile_rows]
    tile_array = [[str(int(column == '#')) for column in row] for row in tile_rows]
    input_tiles[ID] = tile_array

def read_sides(in_tile):
    columns = list(zip(*in_tile))
    side_W = list(columns[0])
    side_E = list(columns[TILE_SIZE-1])
    side_W.reverse()
    side_N = in_tile[0]
    side_S = in_tile[TILE_SIZE-1]
    side_S.reverse()
    sides = [side_N, side_E, side_S, side_W]
    sides = [''.join(side) for side in sides]
    return sides

all_tiles = {}


# for ID in input_dict.keys():


for ID, tile in input_tiles.items():
    tile_sides_binary = read_sides(tile)
    bla = generate_configurations(tile_sides_binary)
    tile_slides_dec = [convert_sides_to_num(sides) for sides in generate_configurations(tile_sides_binary)]
    all_tiles[ID] = tile_slides_dec # {elem for sides in tile_slides_dec for elem in sides}



all_singles = []
for combo in product((0,1,2), repeat=NUMBER_OF_TILES):
    test = []
    for tile, index in zip(all_tiles.values(), combo):
        test += tile[index]
    if len(set(test)) == 4*NUMBER_OF_TILES-12: #48:
        #singles = [ count.key() for count in Counter(test) if count.value() == 1]
        singles=[]
        for key, value in Counter(test).items():
            if value == 1:
                singles.append(key)
        all_singles.append(singles)
        break

# locate the tiles who have two singles
part_1 = 1
for ID, tile in all_tiles.items():
    for configuration in tile:
        count = 0
        for side in configuration:
            count += side in all_singles[0]
        if count == 2:
            part_1 *= int(ID)

print(part_1)
    


#for tile in all_tiles.items():
    
""" combo = []
for tile in all_tiles.values():
    combo += tile[3]
print(len(combo))
print(len(set(combo))) """








# get input dimensions







