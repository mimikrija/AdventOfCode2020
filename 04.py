from itertools import chain
def check_key(passport,key):
    return key in passport.keys()

def are_all_keys_in_passport(passport):
    status = True
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl','ecl', 'pid']:
        status = status and check_key(passport,key)
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
# for passport_value in all_passports:
#     if are_all_keys_in_passport(passport):
#         part_2 += 0

print(f'There are {part_1} valid passports in part 1!')
# There are 230 valid passports in part 1!
