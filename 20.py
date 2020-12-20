# every tile is a dict ID: [side_N, side_E, side_S, side_W]
# I still need to think of a nice convention of writing slide nums
# every tile was rotated and flipped - this means that we don't know the order of N, E, S, W,
# but we do know that two sides are flipped, either N to S or E to W
# in that sense every tile has two possible configurations (we'll worry about rotation later)

# each tile has 10 bits
tile_size = 10 # input array len

def convert_side_to_num(in_string):
    binary = in_string.translate(str.maketrans('#.','10'))
    return int(binary, 2)

def flipped_configurations(in_sides):
    max_num = 2**tile_size - 1
    flipped_v = [] # flipped vertically N-S
    flipped_h = [] # flipped vertically E-W
    for n, side in enumerate(in_sides):
        if n % 2 == 0:
            flipped_v = max_num - side
            flipped_h = side
        else:
            flipped_v = side
            flipped_h = max_num - side
    return [flipped_v, flipped_h]

# all_tiles = {}
# for ID in input_dict.keys():
#     all_tiles[ID] = flipped_configurations(input_dict[ID])

