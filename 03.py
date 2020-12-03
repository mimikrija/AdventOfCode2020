def is_tree(row, column_count):
    return row[column_count%row_length] == "#"

with open('inputs/03') as inputfile:
    inputs = inputfile.readlines()

inputs = [row.strip() for row in inputs]
row_length = len(inputs[0])

part_1 = 0

for column_pos, row in enumerate(inputs):
    part_1 += is_tree(row, column_pos*3)

print(part_1)

