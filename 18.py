import re
from collections import deque

with open('inputs/18') as inputfile:
    inputs = inputfile.readlines()

re_math = re.compile(r'[0-9+*()]')
operations = [ re.findall(re_math, line) for line in inputs]

def calculate_list(in_list):
    if len(in_list) == 1:
        result = in_list[0]
    while len(in_list) >= 3:
        operation = ''
        for c in in_list[:3]:
            operation += c
        result = eval(operation)
        in_list = [str(result)] + in_list[3:]
    return str(result)

def add_brackets(in_list):
    if '+' not in in_list:
        return in_list
    if '*' not in in_list:
        return in_list
    pluses = deque()
    count = 0
    for n, c in enumerate(in_list):
        if c == '+':
            pluses.append(n + count*2)
            break
    if pluses:
        pos = pluses.popleft()
        in_list = [get_rid_of_brackets_2(in_list[:pos-1] + ['('] + in_list[pos-1:pos+2] + [')'] + in_list[pos+2:])]
    return(in_list)

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

def get_rid_of_brackets_2(in_list):
    while '(' in in_list:
        parentheses = deque()
        for n, c in enumerate(in_list):
            if c == '(':
                parentheses.append(n)
            if c == ')':
                pos_2 = n
                pos_1 = parentheses.pop()
                break
        in_list = in_list[:pos_1] + [get_rid_of_brackets_2(in_list[pos_1+1:pos_2])] + in_list[pos_2+1:]
    return (get_rid_of_brackets(add_brackets(in_list)))

part_1 = 0
for operation in operations:
    part_1 += int(get_rid_of_brackets(operation))

print(part_1) # 8929569623593

part_2 = 0
for operation in operations:
    part_2 += int(get_rid_of_brackets_2(operation))

print(part_2) # 231235959382961
