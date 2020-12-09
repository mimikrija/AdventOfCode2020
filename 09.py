with open('inputs/09') as inputfile:
    inputs = inputfile.readlines()

inputs = [int(line.strip()) for line in inputs]


start = 25
end = len(inputs)-1
step = start
part_1 = 0

def is_sum(check_list, number):
    for i, num1 in enumerate(check_list):
        for num2 in check_list[i+1:]:
            if num1 + num2 == number and num1 != num2:
                return True
    return False

for position in range (start,len(inputs)):
    check_in = inputs[position-step:position]
    if not(is_sum(check_in, inputs[position])):
        part_1 = inputs[position]
        break

print(part_1) # 32321523

def is_encryption_weakness(check_list,number):
    return sum(check_list) == number

start = 0
for position in range (start, len(inputs)):
    for size in range (3,len(inputs)):
        check_in = inputs[position:size]
        if is_encryption_weakness(check_in, part_1):
            print(min(check_in),max(check_in), ' = ', min(check_in) + max(check_in))
            break

