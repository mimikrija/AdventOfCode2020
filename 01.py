with open('inputs/01') as inputfile:
    inputs = inputfile.readlines()

inputs = [ int(line.strip()) for line in inputs ]

sums1 = { num1+num2 : num1 * num2 for num1 in inputs for num2 in inputs }



print(f{'Part 1 solution is: {sums1[2020]}')