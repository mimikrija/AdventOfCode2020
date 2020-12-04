
from itertools import chain

with open('inputs/04-ex') as inputfile:
    inputs = inputfile.readlines()


raw_passport_data = [line.strip().split(' ') for line in inputs]

clean_passport_data = []
while [''] in raw_passport_data:
    single_passport = raw_passport_data[0:raw_passport_data.index([''])]
    clean_passport_data.append(single_passport)
    raw_passport_data = raw_passport_data[ raw_passport_data.index([''])+1: ]
clean_passport_data.append(raw_passport_data)


clean_passport_data = [list(chain(*item)) for item in clean_passport_data]
print (len(clean_passport_data))

all_passports = []
for item in clean_passport_data:
    single_passport = {}
    for data in item:
        passport_key, passport_value = data.split(':')
        single_passport[passport_key] = [passport_value]
    all_passports.append(single_passport)



