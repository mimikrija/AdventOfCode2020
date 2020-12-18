import re
from collections import deque

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
    return str(result)

def get_rid_of_brackets(in_list):
    while '(' in in_list:
        parentheses = deque()
        for n, c in enumerate(in_list):
            if c == '(':
                parentheses.append(n)
            if c == ')':
                pos_2 = n
                pos_1 = parentheses.pop()
                break
        in_list = in_list[:pos_1] + [get_rid_of_brackets(in_list[pos_1+1:pos_2])] + in_list[pos_2+1:]
    return (calculate_list(in_list))

for operation in operations:
    print(operation)
    print(get_rid_of_brackets(operation))
