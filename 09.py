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

def yield_func(l):
    total = 0
    for n in l:
        yield total
        total += n

start = 25
step = start

for position in range(start, len(inputs)):
    check_in = inputs[position-step:position]
    if not(is_sum(check_in, inputs[position])):
        part_1 = inputs[position]
        break
import time
a = time.time()*1000

for position in range (0, len(inputs)):
    test = 0
    counter = position
    new_list = yield_func(inputs[position:])
    while test <= part_1:
        test = next(new_list)
        counter += 1 
        if test == part_1:
            break
    if test == part_1:
        print(position, test, counter, min(inputs[position:counter])+max(inputs[position:counter]))
        break
b = time.time()*1000
print(b-a)


print(f'The first number that is not the sum of any two of the 25 numbers before it is {part_1}!')
#print(f'The encryption weakness in my XMAS-encrypted list is: {part_2}!')
# The first number that is not the sum of any two of the 25 numbers before it is 32321523!
# The encryption weakness in my XMAS-encrypted list is: 4794981!
