# Day 13: Shuttle Search

import re

with open('inputs/13') as inputfile:
    inputs = inputfile.readlines()

digits = re.compile(r'[0-9]+')

desired_time = int(inputs[0])
bus_IDs = re.findall(digits, inputs[1])
bus_IDs = [int(bus) for bus in bus_IDs]

all_times = { bus + bus * (desired_time // bus) : bus for bus in bus_IDs }

my_time = min(all_times.keys())
minutes_to_wait = my_time-desired_time

print(f'Part 1 solution is: {minutes_to_wait*all_times[my_time]}!')
# Part 1 solution is: 333!

input_line_two = inputs[1].strip().split(',')
time_diffs = [n for n, c in enumerate(input_line_two) if c != 'x']

def first_overlap(time_start, bus_1, diff_1, bus_2, diff_2, delta):
    for time in range (time_start, bus_1*bus_2*delta+1, delta):
        if (time + diff_1) % bus_1 == 0 and (time + diff_2) % bus_2 == 0:
            return time

time = 0
period = bus_IDs[0]
for n in range(len(bus_IDs)-1):
    b_1 = bus_IDs[n]
    b_2 = bus_IDs[n+1]
    d_1 = time_diffs[n]
    d_2 = time_diffs[n+1]
    time = first_overlap(time, b_1, d_1, b_2,d_2, period)
    period *= b_2 # this should be LCM, but since they're all prime it's the same thing

print(f'First time they align with offsets {time_diffs} is {time}!')
# First time they align with offsets [0, 23, 29, 37, 42, 46, 48, 60, 101] is 690123192779524!
