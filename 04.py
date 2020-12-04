# define passport fields
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required_fields = passport_fields[:-1]

# part 2 sub-sub checks:
def is_str_to_int_in_range(test_value, minimum, maximum):
    try:
        return minimum <= int(test_value) <= maximum
    except:
        return False

# part 2 sub-checks:
def is_byr_valid(test_value):
    return is_str_to_int_in_range(test_value, 1920, 2002)

def is_iyr_valid(test_value):
    return is_str_to_int_in_range(test_value, 2010, 2020)

def is_eyr_valid(test_value):
    return is_str_to_int_in_range(test_value, 2020, 2030)

def is_hgt_valid(test_value):
    if test_value[-2:] == 'cm':
        return is_str_to_int_in_range(test_value[:-2], 150, 193)
    if test_value[-2:] == 'in':
        return is_str_to_int_in_range(test_value[:-2], 59, 76)
    return False

def is_hcl_valid(test_value):
    try:
        int(test_value[1:],16)
        return test_value[0] == '#' and len(test_value) == 7
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

def is_cid_valid(test_value):
    return True

# generate a dictionary of test functions corresponding to passport fields
# so we have everything in one place
passport_checks = { field: eval('is_' + field + '_valid') for field in passport_fields }

# part 1 check
def are_all_keys_in_passport(passport):
    return all(field in passport for field in required_fields)

# part 2 check
def is_passport_valid(passport):
    if not are_all_keys_in_passport(passport):
        return False
    return all(passport_checks[field](value) for field, value in passport.items())


# read & parse input
# 1. read data in bulks split by \n\n
passports_input = open('inputs/04').read().split('\n\n')
# 2. generate a list of consolidated strings per password
passports_input = [passport.strip().split() for passport in passports_input]
# 3. generate a list of dictionaries, each dict represents a single passport
passports = [{data.split(':')[0]: data.split(':')[1] for data in passport} for passport in passports_input]

# solve puzzle
part_1 = 0
part_2 = 0
for passport in passports:
        part_1 += are_all_keys_in_passport(passport)
        part_2 += is_passport_valid(passport)

print(f'There are {part_1} valid passports in part 1!')
print(f'There are {part_2} valid passports in part 2!') #not 175
# There are 230 valid passports in part 1!
# There are 156 valid passports in part 2!
