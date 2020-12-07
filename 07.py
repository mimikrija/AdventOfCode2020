with open('inputs/07-ex') as inputfile:
    inputs = inputfile.readlines()

parents = []
children = []
for line in inputs:
    parent_bag, children_bag = line.strip().split(' bags contain ')
    parents.append(parent_bag)
    children.append(children_bag)
