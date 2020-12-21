with open('inputs/21') as inputfile:
    inputs = inputfile.readlines()

all_foods = []
for line in inputs:
    ingredients, alergens = line.strip().split(' (contains ')
    ingredients = set(ingredients.split(' '))
    alergens = set(alergens[:-1].split(', '))
    all_foods.append((alergens, ingredients))
