# How many fractions lie between 1/3 and 1/2 in the sorted set of 
# reduced proper fractions for d ≤ 12,000?

import math

LIMIT = 12000
red_proper_fractions = []
for num in range(2, LIMIT + 1):
    LOWER_BOUND = math.floor(num / 3)
    UPPER_BOUND = math.ceil(num / 2)
    coprime_list = [i for i in range(LOWER_BOUND, UPPER_BOUND + 1) if math.gcd(i, num) == 1]
    for coprime in coprime_list:
        red_proper_fractions.append(coprime / num)

red_proper_fractions.sort()
third = red_proper_fractions.index(1 / 3)
half = red_proper_fractions.index(1 / 2)

print(half - third - 1)
# answer equals 7295372