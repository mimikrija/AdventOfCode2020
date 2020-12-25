with open('inputs/25') as inputfile:
    inputs = inputfile.readlines()

card_public_key = int(inputs[0].strip())
door_public_key = int(inputs[1].strip())

SUBJECT_NUMBER = 7
DIVIDE_BY = 20201227

def find_loop_size(public_key):
    loop_number = 1
    value = 1
    while True:
        value *= SUBJECT_NUMBER
        value = value % DIVIDE_BY
        if value == public_key:
            break
        else:
            loop_number += 1
    return loop_number

def get_encryption_key(public_key, loop_size):
    value = 1
    for _ in range (loop_size):
        value *= public_key
        value = value % DIVIDE_BY
    return value

card_loop = find_loop_size(card_public_key)
door_loop = find_loop_size(door_public_key)
party_1 = get_encryption_key(card_public_key,door_loop)

print(f'The encryption key is {party_1}!')
# The encryption key is 6408263!
