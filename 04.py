from itertools import chain
def check_key(passport,key):
    return key in passport.keys()

def are_all_keys_in_passport(passport):
    status = True
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl','ecl', 'pid']:
        status = status and check_key(passport,key)
    return status

def is_byr_valid(test_value):
    return 1920 <= int(test_value) <= 2002

def is_iyr_valid(test_value):
    return 2010 <= int(test_value) <= 2020

def is_eyr_valid(test_value):
    return 2020 <= int(test_value) <= 2030

def is_hgt_valid(test_value):
    if test_value[-2:] == 'cm':
        return 150 <= int(test_value[:-2]) <= 193
    if test_value[-2:] == 'in':
        return 59 <= int(test_value[:-2]) <= 76
    return False

def is_hcl_valid(test_value):
    try:
        int(test_value[1:],16)
        return test_value[0] == '#' and len(test_value)==7
    except:
        return False

def is_ecl_valid(test_value):
    return test_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return False


def is_pid_valid(test_value):
    try:
        int(test_value)
        return len(test_value) == 9
    except:
        return False

def is_value_valid(key,test_value):
        if key == 'byr':
            return is_byr_valid(test_value)
        if key == 'iyr':
            return is_iyr_valid(test_value)
        if key == 'eyr':
            return is_eyr_valid(test_value)
        if key == 'hgt':
            return is_hgt_valid(test_value)
        if key == 'hcl':
            return is_hcl_valid(test_value)
        if key == 'ecl':
            return is_ecl_valid(test_value)
        if key == 'pid':
            return is_pid_valid(test_value)
        if key == 'cid':
            return True

def is_passport_valid(passport):
    status = True
    for field, value in passport.items():
        status = status and is_value_valid(field, value)
    return status


with open('inputs/04') as inputfile:
    inputs = inputfile.readlines()


raw_passport_data = [line.strip().split(' ') for line in inputs]
clean_passport_data = []
while [''] in raw_passport_data:
    single_passport = raw_passport_data[0:raw_passport_data.index([''])]
    clean_passport_data.append(single_passport)
    raw_passport_data = raw_passport_data[ raw_passport_data.index([''])+1: ]
clean_passport_data.append(raw_passport_data)



clean_passport_data = [list(chain(*item)) for item in clean_passport_data]

all_passports = []
for item in clean_passport_data:
    single_passport = {}
    for data in item:
        passport_key, passport_value = data.split(':')
        single_passport[passport_key] = passport_value
    all_passports.append(single_passport)


part_1 = 0
for passport in all_passports:
    part_1 += are_all_keys_in_passport(passport)

part_2 = 0
for passport in all_passports:
    if are_all_keys_in_passport(passport):
        part_2 += is_passport_valid(passport)


print(f'There are {part_1} valid passports in part 1!')
print(f'There are {part_2} valid passports in part 2!') #not 175
# There are 230 valid passports in part 1!
# There are 156 valid passports in part 2!

