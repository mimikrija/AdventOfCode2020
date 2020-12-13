import re

with open('inputs/13-ex') as inputfile:
    inputs = inputfile.readlines()

digits = re.compile(r'[0-9]+')

desired_time = int(inputs[0])
bus_IDs = re.findall(digits, inputs[1])
bus_IDs = [ int(bus) for bus in bus_IDs]

all_times = { bus + bus * (desired_time // bus) : bus for bus in bus_IDs }

my_time = min(all_times.keys())
minutes_to_wait = my_time-desired_time

print(f'Part 1 solution is: {minutes_to_wait*all_times[my_time]}!') # 333

# part 2

# def sum_until():
#     time = 1068779
#     is_it = ((time+inc)%bus == 0  for inc, bus in zip(time_diffs, bus_IDs))
#     print(all(is_it))
#     yield all(is_it), time
#     time += 1

input_line_two = inputs[1].strip().split(',')

time_diffs = [n for n, c in enumerate(input_line_two) if c != 'x']
# print(bus_IDs)

buses_and_increments = zip(time_diffs, bus_IDs)
print(time_diffs)
mali = bus_IDs[0]
print(bus_IDs)
prvo_rjesenje = [(0,bus_IDs[0])]
for inc, veliki in zip(time_diffs, bus_IDs):
    if inc == mali or mali == veliki:
        continue
    for n in range (1000000):
        proba = (n * veliki) // mali
        if proba > 0:
            test = proba * mali
            if n * veliki == test + inc:
                #print(mali, veliki, inc,': ', test)
                prvo_rjesenje.append((test, veliki))
                break
    #print('--------')

prvo_rjesenje
print(prvo_rjesenje)

for n in range(0,7*13,7):
    if n%13 == 1:
        print(n)
        for m in range(4, 7*13*59, 59):
            if m%(7*13) == n:
                print(m)
                for q in range (6, 7*13*59*31, 31):
                    if q%(7*13*59) == m:
                        print(q)
                        for p in range (7, 7*13*59*31*19, 19):
                            if p%(7*13*59*31) == q:
                                print(p)
                                quit()


for n in range (1, 59*13, 13):
    if n % 59 == 4:
        first = n
        break

print(first)

for n in range (7, 19*59*13, 19):
    if n % (13*59) == first:
        second = n
        break
print(second)

# for n in range (0, 13*59*19*7, 7):
#     if n % (13*59*19) == second:
#         third = n
#         break

print(third)

for n in range (6, 31*19*59*13, 31):
    if n%(13*59*19) == second:
        fourth = n
        break

print(fourth)


for n in range (1, 11*35, 11):
    if n % 35 == 17:
        print(n)


for n in range (2, 35, 5):
    if n % 7 == 3:
        print(n)


for n in range (1, 11*35, 11):
    if n % 35 == 17:
        print(n)
print(122%5, 122%7, 122% 11)
quit()

solution_one = [ (i,j)  for j in range (17,400,17) for i in range (6+13*j//17,300)
            if 17*i == 102+13*j]
# a = next(solution_one)
# b = next(solution_one)
# print(a, b)
def time(base, inc, n):
    return base + inc*n+1

for i in range(19,300, 13):
    for j in range(0,400,17):
        if 17*i == 102*13*j:
            print(i,j, 17*j)

#print(solution_one)
quit()

solution_two = ( 187 + 19*i for i,j in zip(range(19,100000,13),range(17,100000,17))
            if 187 + 19*i == 323 + 221*j)

print(next(solution_two))
print(next(solution_two))
quit()

lista_prva = (7*j for i in range(1,10000) for j in range (1,10000)
    if 13 * i + 77 == 7 * j)
print (next(lista_prva))
#print (next(lista_prva))
#print (next(lista_prva))

lista_druga = (31 * j + 56 for i in range(1,10000) for j in range (1,10000)
    if 59 * i + 350 == 31 * j + 56)
print (next(lista_druga))
#print (next(lista_druga))
#print (next(lista_druga))

print('----------')

lista_treca = (168+i*91 for i in range(1,100000) for j in range (1,100000)
    if 168 + i * 91 == 350+59*j)
print (next(lista_treca))
#print (next(lista_treca))
#print (next(lista_treca))

lista_cetvrta = (350+59*j for i in range(1,100000) for j in range (1,100000)
    if 5719+5369*i == 350+59*j)
print (next(lista_cetvrta))
print (next(lista_cetvrta))
print('--------')
lista_cetvrta = (133+19*j for i in range(1,100000) for j in range (1,100000)
    if 11088+5369*i == 133+19*j)
print (next(lista_cetvrta))
print (next(lista_cetvrta))
# ok ovo ce izgenerirati sve parove i,j-ova koji zadovoljavaju uvjet
# ovi rubovi se temelje na prvim rjesenjima i razlici izmedju njih na gornje dvije liste
# lista_druga = ((i,j,13 * i + 77 == 31 * j + 56) for i,j in zip(range(27,10000,31),range (12,10000,13)))
# print (next(lista_druga))
# print (next(lista_druga))



# for i in range (10000):
#     for j in range (10000):
#         if 13 * i + 77 == 59 *j + 350:
#             print('evo me')
#             break

# print ( 1068781 / 23100)
# print ( 1068781 / 60606)
# for inc, bus in zip(time_diffs, bus_IDs):
#     print((1068781+inc)/bus)

#quit()
# start_time = max(bus_IDs)
# smallest_inc = min(bus_IDs)
# time = 1000000

# is_it = sum_until()
# while True:
#     status, time1 = next(is_it)
#     if status:
#         print(time1)
#         break
        
# quit()
# for time in range(1068779,1068779+100):
#     is_it = ((time+inc)%bus == 0  for inc, bus in zip(time_diffs, bus_IDs))
#     if all(is_it):
#         print(time)
#         break


