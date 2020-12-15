import re

with open('inputs/13-ex') as inputfile:
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

buses_and_increments = zip(time_diffs, bus_IDs)
#print(list(buses_and_increments))
print(time_diffs)
print(bus_IDs)

for n, pair in enumerate(buses_and_increments):
    print (pair)
