def is_tree(row, column):
    # if column is out of range, the map continues hence %
    return row[column%row_length] == "#"

def tree_count(rows, ratio):
    delta_column, delta_row = ratio
    count = 0
    for row_n, row in enumerate(rows):
        if row_n%delta_row == 0:
            count += is_tree(row, (row_n*delta_column)//delta_row)
    return count

with open('inputs/03') as inputfile:
    rows = inputfile.readlines()

rows = [row.strip() for row in rows]
row_length = len(rows[0])

ratios_to_check = [(c,r) for r in range (1,3) for c in range (1,8,2) if r != 2 or c < r]
# [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] (part 2 ratios to check)

all_ratios_tree_count = [tree_count(rows, ratio) for ratio in ratios_to_check]

part_1 = all_ratios_tree_count[1]
part_2 = 1
for count in all_ratios_tree_count:
    if count != 0:
        part_2 *= count


print(f'Part 1 solution is: {part_1}')
print(f'Part 2 solution is: {part_2}')
# Part 1 solution is: 292!
# Part 2 solution is: 9354744432!
