def is_tree(row, column_count):
    return row[column_count%row_length] == "#"

def tree_count(rows, column_multiplier, row_multiplier):
    count = 0
    for row_n, row in enumerate(inputs):
        if row_n%row_multiplier == 0:
            count += is_tree(row, row_n*column_multiplier//row_multiplier)
    return count

with open('inputs/03') as inputfile:
    inputs = inputfile.readlines()

inputs = [row.strip() for row in inputs]
row_length = len(inputs[0])

ratios_to_check = [ (c,r) for r in range (1,3) for c in range (1,8,2) if r != 2 or c < r ]
# [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] (part 2 ratios to check)

for slope in slopes:
    temp_2 = 0
    for column_pos, row in enumerate(inputs):
        temp_2 += is_tree(row, column_pos*slope)
    if temp_2 > 0:
        part_2 *= temp_2


temp_2 = 0
for column_pos, row in enumerate(inputs):
    if column_pos%2 == 0:
        temp_2 += is_tree(row, column_pos//2)

if temp_2 > 0:
    part_2 *= temp_2


print(f'Part 1 solution is: {part_1}! {part_1 == 292}')
print(f'Part 2 solution is: {part_2}! {part_2 == 9354744432}')
# Part 1 solution is: 292!
# Part 2 solution is: 9354744432!
