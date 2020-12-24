HEX_DIRECTIONS = {
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
     'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
     'w': (-1, 1, 0)
}

def hex_add(in_hex_a, in_hex_b):
    return tuple(coordinate_a+ coordinate_b for coordinate_a, coordinate_b in zip(in_hex_a, in_hex_b))

