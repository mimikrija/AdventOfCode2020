import re

with open('inputs/02-ex') as inputfile:
    inputs = inputfile.readlines()

words =re.compile(r'\w+')

rules = []
for line in inputs:
    rules.append(re.findall(words,line))

