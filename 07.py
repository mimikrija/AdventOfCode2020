with open('inputs/07') as inputfile:
    inputs = inputfile.readlines()

everything = [line.strip() for line in inputs]


find_next = ['shiny gold']

part_1 = 0
all_solutions = []
def find_bags(find_next, all_solutions):
    while find_next != []:
        for bag in find_next:
            find_next = [rule.split(' bags contain')[0] for rule in everything if bag in rule and rule.find(bag) != 0]
            find_bags(find_next,all_solutions)
            all_solutions += find_next
    return len(set(all_solutions))

print(find_bags(find_next,[])) #246
