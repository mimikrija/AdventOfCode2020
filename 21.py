from collections import Counter
with open('inputs/21') as inputfile:
    inputs = inputfile.readlines()

all_foods = []
for line in inputs:
    ingredients, alergens = line.strip().split(' (contains ')
    ingredients = set(ingredients.split(' '))
    alergens = set(alergens[:-1].split(', '))
    all_foods.append((alergens, ingredients))

potential_alergens = {}
ALL_INGREDIENTS = set()
ALL_ALERGENS = set()
for alergens, ingredients in all_foods:
    for alergen in alergens:
        if alergen not in potential_alergens.keys():
            potential_alergens[alergen] = ingredients
        else:
            potential_alergens[alergen].union(ingredients)
    ALL_INGREDIENTS = ALL_INGREDIENTS.union(ingredients)
    ALL_ALERGENS = ALL_ALERGENS.union(alergens)


found_alergens = {}
while potential_alergens:
    for alergen in ALL_ALERGENS:
        result = ALL_INGREDIENTS.copy()
        for alergens, ingredients in all_foods:
            if alergen in alergens:
                result = result.intersection(ingredients)
        if len(result) == 1:
            solution = result.pop()
            for key, value in potential_alergens.items():
                if solution in value:
                    potential_alergens[key].remove(solution)
            found_alergens[alergen] = solution
            del potential_alergens[alergen]


not_alergens = ALL_INGREDIENTS.difference(found_alergens.values())
part_1 = 0

for _, ingredients in all_foods:
    for ingredient in ingredients:
        part_1 += ingredient in not_alergens

print(part_1)
# 1977

part_2 = ','.join(item for item in sorted(found_alergens))

print(part_2)
# dairy,eggs,fish,nuts,peanuts,sesame,shellfish,wheat
