import re

with open('inputs/18-ex') as inputfile:
    inputs = inputfile.readlines()

re_math = re.compile(r'[0-9+*()]')
operations = [ re.findall(re_math, line) for line in inputs]

def calculate_list(in_list):
    while len(in_list) >= 3:
        operation = ''
        for c in in_list[:3]:
            operation += c
        result = eval(operation)
        in_list = [str(result)] + in_list[3:]
    return result
