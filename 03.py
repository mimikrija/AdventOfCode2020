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

part_1 = 0
part_2 = 1
slopes = [1, 3, 5, 7]
position_counter = 0


for column_pos, row in enumerate(inputs):
    part_1 += is_tree(row, column_pos*3)


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
