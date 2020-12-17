import re
import math

with open('inputs/13') as inputfile:
    inputs = inputfile.readlines()

digits = re.compile(r'[0-9]+')

desired_time = int(inputs[0])
bus_IDs = re.findall(digits, inputs[1])
bus_IDs = [ int(bus) for bus in bus_IDs]

all_times = { bus + bus * (desired_time // bus) : bus for bus in bus_IDs }

my_time = min(all_times.keys())
minutes_to_wait = my_time-desired_time

print(f'Part 1 solution is: {minutes_to_wait*all_times[my_time]}!') # 333

# part 2

# def sum_until():
#     time = 1068779
#     is_it = ((time+inc)%bus == 0  for inc, bus in zip(time_diffs, bus_IDs))
#     print(all(is_it))
#     yield all(is_it), time
#     time += 1

input_line_two = inputs[1].strip().split(',')

time_diffs = [ n for n, c in enumerate(input_line_two) if c != 'x']

print(time_diffs)
print(bus_IDs)

def chinese_remainder(numbers, remainders):
    result = 0
    product = math.prod(numbers)
    prod_div_by_reminders = [product // remainder for remainder in remainders]
    mod_mult_inverse = [(prod_div_by_reminders[n] * remainders[n])%numbers[n]
            for n in range(len(numbers))]
    for n in range(len(numbers)):
        result+= (remainders[n]*prod_div_by_reminders[n]*mod_mult_inverse[n])
    return result%product

part2 = chinese_remainder(bus_IDs[1:],time_diffs[1:])
print(part2) # 30309578578160 not correct
print(part2%29)
for n,r in list(zip(bus_IDs,time_diffs)):
    if n != 0:
        print(n, part2%int(n),r)
print((part2*9)%443)


# 181857471544305 not correct
