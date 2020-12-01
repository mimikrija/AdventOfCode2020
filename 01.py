with open('inputs/01') as inputfile:
    inputs = inputfile.readlines()

inputs = [ int(line.strip()) for line in inputs ]

part1 = { num1 + num2 : num1 * num2 for num1 in inputs for num2 in inputs }
part2 = { num1 + num2 + num3 : num1 * num2 * num3 for num1 in inputs for num2 in inputs for num3 in inputs}

print(f'Part 1 solution is: {part1[2020]}!')
print(f'Part 2 solution is: {part2[2020]}!')
# Part 1 solution is: 388075!
# Part 2 solution is: 293450526!
