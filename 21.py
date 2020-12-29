from collections import Counter
with open('inputs/21') as inputfile:
    inputs = inputfile.readlines()

# parse input into all_foods (list of tupples (alergens, ingredients))
# and into constant sets of all ingredients and all alergens
all_foods = []
ALL_INGREDIENTS = set()
ALL_ALERGENS = set()
for line in inputs:
    ingredients, alergens = line.strip().split(' (contains ')
    ingredients = set(ingredients.split(' '))
    alergens = set(alergens[:-1].split(', '))
    all_foods.append((alergens, ingredients))
    ALL_INGREDIENTS = ALL_INGREDIENTS.union(ingredients)
    ALL_ALERGENS = ALL_ALERGENS.union(alergens)


# generate dictionary of potential alergens
# {alergen: {potentialy dangerous foods}}
potential_alergens = dict()
for alergen in ALL_ALERGENS:
    # in theory, everything is an alergen
    dangerous_ingredients = ALL_INGREDIENTS.copy()
    for listed_alergens, ingredients in all_foods:
        # but only if the alergen we are looking for is listed for this food
        if alergen in listed_alergens:
            # .. the ingredients that food contains potentially contain this alergen
            dangerous_ingredients = dangerous_ingredients.intersection(ingredients)
    potential_alergens[alergen] = dangerous_ingredients

# keep eliminating as long as the number of determined alergens
# is less than number of total alergens
determined_alergens = dict()
while len(determined_alergens) < len(ALL_ALERGENS):
    for alergen, potential_ingredients in potential_alergens.items():
        # eliminate already determined ingredients from the potential ingredients
        candidates = potential_ingredients.difference(set(determined_alergens.values()))
        if len(candidates) == 1:
            determined_alergens[alergen] = candidates.pop()

not_alergens = ALL_INGREDIENTS.difference(set(determined_alergens.values()))
part_1 = 0

for _, ingredients in all_foods:
    for ingredient in ingredients:
        part_1 += ingredient in not_alergens


part_2 = ','.join(item for item in sorted(determined_alergens))

print(f'Non-alergens appear in my list of foods {part_1} times!')
# Non-alergens appear in my list of foods 1977 times!


print(f'The list of my dangerous ingredients is: {part_2}')
# The list of my dangerous ingredients is: dairy,eggs,fish,nuts,peanuts,sesame,shellfish,wheat!
