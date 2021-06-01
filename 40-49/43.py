# Find the sum of all 0 to 9 pandigital numbers with this property ...

import itertools

pandigital = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
pandigital_copy = []
for tup in pandigital:
    if (tup[0] != '0'):
        string = ''.join(tup)
        pandigital_copy.append(string)

substring_divisible = []
for num in pandigital_copy:
    if (int(num[7:10]) % 17 == 0 and int(num[6:9]) % 13 == 0 and \
        int(num[5:8]) % 11 == 0 and int(num[4:7]) % 7 == 0 and \
        int(num[3:6]) % 5 == 0 and int(num[2:5]) % 3 == 0 and \
        int(num[1:4]) % 2 == 0):
        substring_divisible.append(int(num))

print(sum(substring_divisible))
# answer equals 16695334890

