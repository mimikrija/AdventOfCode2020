import re

with open('inputs/18-ex') as inputfile:
    inputs = inputfile.readlines()

re_math = re.compile(r'[0-9+*()]')
operations = [ re.findall(re_math, line) for line in inputs]
