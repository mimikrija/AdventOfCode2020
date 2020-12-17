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


def de_acitivation(cube, positions):
    # inactive becomes active
    if positions.get(cube, '.') == '#' and count_neighbors(cube, positions) in {2, 3}:
        positions[cube] = '.'
    # active becomes inactive
    if positions.get(cube, '.') == '.' and count_neighbors(cube, positions) == 3:
        positions[cube] = '#'



