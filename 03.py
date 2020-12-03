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

ratios_to_check = [(c,r) for r in range (1,3) for c in range (1,8,2) if r != 2 or c < r]
# [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] (part 2 ratios to check)

all_ratios_tree_count = [tree_count(inputs,*ratio) for ratio in ratios_to_check]

part_1 = all_ratios_tree_count[1]
part_2 = 1
for count in all_ratios_tree_count:
    if count != 0:
        part_2 *= count


print(f'Part 1 solution is: {part_1}')
print(f'Part 2 solution is: {part_2}')
# Part 1 solution is: 292!
# Part 2 solution is: 9354744432!
