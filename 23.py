input_cups = '389125467'
CIRCLE_SIZE = len(input_cups)

# linked dictionary
cups_circle = {}
for n, cup in enumerate(input_cups):
    cups_circle[int(cup)] = int(input_cups[(n+1)%CIRCLE_SIZE])
