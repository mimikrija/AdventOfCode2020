import re
from math import sqrt
from copy import deepcopy
from collections import Counter
from operator import mul
from functools import reduce

def convert_sides_to_num(in_sides):
    return [int(side,2) for side in in_sides]

def generate_configurations(in_sides):
    # there are 4 possible configurations: original/rotated, flipped horizontally, flipped vertically, fliped both
    # flipped both reduces to rotation, so we don't care about that one
    # flipped vertically and flipped horizontally differ only by two rotations
    # the property of any flipped configuration is that *ALL* the sides are reversed (and their order is reversed as well)
    # the property of any non-flipped configuration is that *ALL* the sides are not reversed.
    # hence (for matching purposes) it is enough to generate a list of sides and a list of flipped sides
    flipped = reversed([''.join(reversed(side)) for side in in_sides])
    return [in_sides, flipped]

def read_sides(in_tile):
    """ reads each side of `in_tile` from left to right and
    returns a list of four tiles """
    columns = list(zip(*in_tile))
    side_W = list(columns[0])
    side_E = list(columns[TILE_SIZE-1])
    side_W.reverse()
    side_N = in_tile[0].copy()
    side_S = in_tile[TILE_SIZE-1].copy()
    side_S.reverse()
    sides = [side_N, side_E, side_S, side_W]
    sides = [''.join(side) for side in sides]
    return sides

def compare_tiles(ID_fixed, ID_possible_match, tiles_dict):
    """ checks if any of the sides in `ID_fixed` mathes with any
    of the sides in possible configurations of `ID_possible_match`"""
    sides_to_look_at = tiles_dict[ID_fixed][0]
    for sides in tiles_dict[ID_possible_match]:
        for side in sides:
            if side in sides_to_look_at:
                return True
    return False

def rotate_clockwise(in_matrix):
    return [[in_matrix[j][i] for j in range(len(in_matrix[0])-1,-1,-1)] for i in range(len(in_matrix))]

def flip(in_matrix):
    return [[in_matrix[i][j] for j in range(len(in_matrix[0])-1,-1,-1)] for i in range(len(in_matrix))]


# read input from file
re_numbers = re.compile(r'\d+')
inputs = open('inputs/20').read().split('\n\n')

# define tile/final image constants
NUMBER_OF_TILES = len(inputs)
IMAGE_SIDE_SIZE = int(sqrt(NUMBER_OF_TILES))
TILE_SIZE = len(inputs[0].split('\n')[0])

# parse input into dict of tiles {ID: actual tile image from input file
# with '#' converted to '1' and '.' converted to '0'}
input_tiles = {}
for tile in inputs:
    tile_data = tile.split('\n')
    ID = int(re.findall(re_numbers, tile_data[0])[0])
    tile_rows = tile_data[1:]
    tile_array = [[str(int(column == '#')) for column in row] for row in tile_rows]
    input_tiles[ID] = tile_array

# generate a dictionary which maps tile IDs to a list of possible configurations,
# where possible configurations are lists of slide numbers, and slide numbers flipped
tiles_sides_only = { ID: [convert_sides_to_num(sides) for sides in generate_configurations(read_sides(tile))] for ID, tile in input_tiles.items() }


# generate a dictionary of matched tiles:
# {ID: set of matching tiles}
matched_tiles = {}
for ID_to_compare_to in tiles_sides_only.keys():
    for candidate_ID in tiles_sides_only.keys():
        if candidate_ID == ID_to_compare_to:
            continue
        else:
            if compare_tiles(ID_to_compare_to, candidate_ID, tiles_sides_only):
                if ID_to_compare_to in matched_tiles:
                    matched_tiles[ID_to_compare_to].add(candidate_ID)
                else:
                    matched_tiles[ID_to_compare_to] = set([candidate_ID])


# split matched tiles into three different categories
corners = {ID: match for ID, match in matched_tiles.items() if len(match) == 2}


# party 1 solution: multiply IDs of corner tiles
party_1 = reduce(mul, (tile for tile in corners))

print(f'Multiplied corner IDs: {" * ".join(str(tile) for tile in corners)} = {party_1}!')
# Multiplied corner IDs: 1867 * 2441 * 2633 * 1663 = 19955159604613!

# find 'relative' top-left corner
matched_corner_sides = {corner_ID: [] for corner_ID in corners}
for corner_ID, matches in corners.items():
    for matched_ID in matches:
        for num_slide, fixed_side in enumerate(tiles_sides_only[corner_ID][0]):
            for n, configuration in enumerate(tiles_sides_only[matched_ID]):
                for pos, side in enumerate(configuration):
                    if side == fixed_side:
                        if n == 0:
                            relative_flipped = True
                        else:
                            relative_flipped = False
                        relative_rotation = 3 - pos
                        #print(f'{corner_ID}, slide no. {num_slide}, matched with: {matched_ID}, flipped: {relative_flipped}, and rotated by {relative_rotation}')
                        matched_corner_sides[corner_ID].append([num_slide, matched_ID, relative_flipped, relative_rotation])

# find upper left if exists (luckily it does both for my input and test input so
# I'll just go along with it)

assembly = {}
# semi manually put relative_upper_left into assembly/oriented tiles:
for corner_ID, matched in matched_corner_sides.items():
    if (matched[0][0] == 1 and matched[1][0] == 2) or (matched[0][0] == 2 and matched[1][0] == 1):
        relative_upper_left = corner_ID
        assembly[corner_ID] = (0,0) # add global position of the tile

oriented_tiles = {}
oriented_tiles[relative_upper_left] = input_tiles[relative_upper_left]


def match_tile(fixed_tile, tile, fixed_coordinate):
    test_tile = deepcopy(tile)
    for _ in range(4):
        # check vertical match
        if fixed_tile[TILE_SIZE-1] == test_tile[0]:
            match_type = 'vertical'
            break
        # check horizontal match
        if all(fixed_tile[c][TILE_SIZE-1] == test_tile[c][0] for c in range(TILE_SIZE)):
            match_type = 'horizontal'
            break
        original_conf = deepcopy(test_tile)
        test_tile = flip(test_tile)
        # check vertical match
        if fixed_tile[TILE_SIZE-1] == test_tile[0]:
            match_type = 'vertical'
            break
        # check horizontal match
        if all(fixed_tile[c][TILE_SIZE-1] == test_tile[c][0] for c in range(TILE_SIZE)):
            match_type = 'horizontal'
            break
        test_tile = rotate_clockwise(original_conf)

    if match_type == 'vertical':
        coordinate = (fixed_coordinate[0]+1, fixed_coordinate[1])
    if match_type == 'horizontal':
        coordinate = (fixed_coordinate[0], fixed_coordinate[1]+1)
    
    return coordinate, test_tile


while len(assembly) < NUMBER_OF_TILES:
    # find tiles in the assembly which still need to be matched
    available_tiles_for_matching = {tile for tile in assembly if not all(matched_tile in assembly for matched_tile in matched_tiles[tile])}
    for fixed_tile in available_tiles_for_matching:
        candidates = set(matched_tiles[fixed_tile]).difference(set(assembly))
        for tile in candidates:
            assembly[tile], oriented_tiles[tile] = match_tile(oriented_tiles[fixed_tile], input_tiles[tile], assembly[fixed_tile])

def remove_borders(in_matrix):
    return [line[1:len(line)-1] for line in in_matrix[1:len(in_matrix)-1]]

tiles_without_borders = {ID: remove_borders(tile) for ID, tile in oriented_tiles.items()}

final_image = [[(i,j) for i in range(IMAGE_SIDE_SIZE)] for j in range(IMAGE_SIDE_SIZE)]





for ID, coordinate in assembly.items():
    row, column = coordinate
    final_image[row][column] = remove_borders(oriented_tiles[ID])

# flatten matrix
final_image_flat = []
for mr, main_row in enumerate(final_image):
    for subrow in range(TILE_SIZE-2): # take into acount removed borders
        line = []
        for n in range(len(main_row)):
            line += main_row[n][subrow]
        final_image_flat.append(line)

# define monster constants
MONSTER_TOP =    "                  # "
MONSTER_MIDDLE = "#    ##    ##    ###"
MONSTER_BOTTOM = " #  #  #  #  #  #   "
# relative offsets of hashes in the monster string
MONSTER_TOP_REL_POS = [pos for pos, c in enumerate(MONSTER_TOP) if c == "#"]
MONSTER_MIDDLE_REL_POS = [pos for pos, c in enumerate(MONSTER_MIDDLE) if c == "#"]
MONSTER_BOTTOM_REL_POS = [pos for pos, c in enumerate(MONSTER_BOTTOM) if c == "#"]
# line limit we don't want to search after because the monster won't fit
LINE_LIMIT = max(MONSTER_BOTTOM_REL_POS + MONSTER_MIDDLE_REL_POS + MONSTER_TOP_REL_POS)
# total number of "#" symbols per monster (we need that for the final result)
HASHES_PER_MONSTER = len(MONSTER_TOP_REL_POS) + len(MONSTER_MIDDLE_REL_POS) + len(MONSTER_BOTTOM_REL_POS)


def count_monsters(in_image):
    """ returns the total count of monsters in `in_image` """

    character_matches = lambda line, loc : line[loc] == '1'
    monster_count = 0
    for mid in range(1, len(in_image)-2):
        top_line = in_image[mid-1]
        middle_line = in_image[mid]
        bottom_line = in_image[mid+1]
        combo_tuples = ((top_line, MONSTER_TOP_REL_POS), (middle_line, MONSTER_MIDDLE_REL_POS), (bottom_line, MONSTER_BOTTOM_REL_POS))
        for pos in range (len(middle_line)-LINE_LIMIT):
            if all(character_matches(line, pos+offset) for line, offsets in combo_tuples for offset in offsets):
                monster_count += 1
    return monster_count

def find_monsters(in_image):
    """ change `in_image` configurations until a configuration is found
    which actually has monsters in it """
    attempted_image = in_image
    for _ in range(4):
        attempted_image = rotate_clockwise(attempted_image)
        monster_count = count_monsters(attempted_image)
        if monster_count > 0:
            return monster_count
    attempted_image = flip(attempted_image)
    for _ in range(4):
        attempted_image = rotate_clockwise(attempted_image)
        monster_count = count_monsters(attempted_image)
        if monster_count > 0:
            return monster_count
    return 0



all_hashes_in_image = sum(c=="1" for line in final_image_flat for c in line)
monster_count = find_monsters(final_image_flat)

party_2 = all_hashes_in_image - monster_count * HASHES_PER_MONSTER

print(f'monster count is {monster_count == 21}!')
print(f'Party 2 solution, the "sea roughness" is {party_2 == 1639}!')
