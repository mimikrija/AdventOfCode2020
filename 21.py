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
for alergens, ingredients in all_foods:
    for alergen in alergens:
        if alergen not in potential_alergens.keys():
            potential_alergens[alergen] = ingredients
        else:
            potential_alergens[alergen].union(ingredients)
    ALL_INGREDIENTS = ALL_INGREDIENTS.union(ingredients)
