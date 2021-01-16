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

def sum_until(check_list):
    total = 0
    for pos, num in enumerate(check_list):
        yield total, pos
        total += num

def find_encryption_weakness(test_value):
    current_sum = 0
    list_to_test = sum_until(inputs[start_pos:])
    while current_sum <= test_value:
        current_sum, end_pos = next(list_to_test)
        end_pos += start_pos
        if current_sum == test_value:
            return min(inputs[start_pos:end_pos]) + max(inputs[start_pos:end_pos])

start = 25
step = start

for position in range(start, len(inputs)):
    check_in = inputs[position-step:position]
    if not(is_sum(check_in, inputs[position])):
        part_1 = inputs[position]
        break

for start_pos in range (0, len(inputs)):
    part_2 = find_encryption_weakness(part_1)
    if part_2 != None:
        break


print(f'The first number that is not the sum of any two of the 25 numbers before it is {part_1}!')
print(f'The encryption weakness in my XMAS-encrypted list is: {part_2}!')
# The first number that is not the sum of any two of the 25 numbers before it is 32321523!
# The encryption weakness in my XMAS-encrypted list is: 4794981!
