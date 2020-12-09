with open('inputs/09') as inputfile:
    inputs = inputfile.readlines()

inputs = [int(line.strip()) for line in inputs]

def is_sum(check_list, number):
    """ Check if the sum of any two numbers in `check_list` equals to `number` """
    for i, num1 in enumerate(check_list):
        for num2 in check_list[i+1:]:
            if num1 + num2 == number and num1 != num2:
                return True
    return False

start = 25
step = start
part_1 = 0

for position in range(start, len(inputs)):
    check_in = inputs[position-step:position]
    if not(is_sum(check_in, inputs[position])):
        part_1 = inputs[position]
        break

for position in range (0, len(inputs)):
    for size in range (3, len(inputs)):
        # create a sublist of size 2+
        check_in = inputs[position:size]
        # skip further creation of sublists:
        if sum(check_in) >= part_1:
            break
    if sum(check_in) == part_1:
        part_2 = min(check_in) + max(check_in)
        break

print(f'The first number that is not the sum of any two of the 25 numbers before it is {part_1}!')
print(f'The encryption weakness in my XMAS-encrypted list is: {part_2}!')
# The first number that is not the sum of any two of the 25 numbers before it is 32321523!
# The encryption weakness in my XMAS-encrypted list is: 4794981!
