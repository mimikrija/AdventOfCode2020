# Day 3: Toboggan Trajectory

def is_tree(row, column):
    # if column is out of range, the map continues hence %
    return row[column%row_length] == "#"

def get_column_position(row_number, slope):
    delta_column, delta_row = slope
    return row_number * delta_column // delta_row
    # we need to divide by delta_row in case it is > 1
    # otherwise we would end up with a smaller slope

def tree_count(rows, slope):
    _, delta_row = slope
    count = 0
    for row_number in range(0, len(rows), delta_row):
        count += is_tree(rows[row_number], get_column_position(row_number, slope))
    return count

with open('inputs/03') as inputfile:
    rows = inputfile.readlines()

rows = [row.strip() for row in rows]
row_length = len(rows[0])

slopes_to_check = [(c,r) for r in range (1,3) for c in range (1,8,2) if r != 2 or c < r]
# [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] (part 2 slopes to check)

all_slopes_tree_count = [tree_count(rows, slope) for slope in slopes_to_check]

part_1 = all_slopes_tree_count[1]
part_2 = 1
for count in all_slopes_tree_count:
    if count != 0:
        part_2 *= count


print(f'Part 1 solution is: {part_1}')
print(f'Part 2 solution is: {part_2}')
# Part 1 solution is: 292!
# Part 2 solution is: 9354744432!
