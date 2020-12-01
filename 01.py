with open('inputs/01') as inputfile:
    inputs = inputfile.readlines()

inputs = [int(line.strip()) for line in inputs]

part1 = {num1 + num2 : num1 * num2
        for i, num1 in enumerate(inputs)
        for num2 in inputs[i+1:]}

part2 = {num1 + num2 + num3 : num1 * num2 * num3
        for i, num1 in enumerate(inputs)
        for j, num2 in enumerate(inputs[i+1:])
        for num3 in inputs[j+1:]}

print(f'Part 1 solution is: {part1[2020]}!')
print(f'Part 2 solution is: {part2[2020]}!')
# Part 1 solution is: 388075!
# Part 2 solution is: 293450526!
