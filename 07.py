with open('inputs/07-ex') as inputfile:
    inputs = inputfile.readlines()

for line in inputs:
    parent_bags, children_bags = line.split('contain')
