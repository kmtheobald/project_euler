# By listing the set of reduced proper fractions for d ≤ 1,000,000 in 
# ascending order of size, find the numerator of the fraction 
# immediately to the left of 3/7.

import math
from fractions import Fraction

LIMIT = 1000000
red_proper_fractions = []
for num in range(2, LIMIT + 1):
    LOWER_BOUND = math.floor(0.42856 * num)
    UPPER_BOUND = math.ceil(0.42858 * num)
    coprime_list = [i for i in range(LOWER_BOUND, UPPER_BOUND + 1) \
        if math.gcd(i, num) == 1]
    for coprime in coprime_list:
        red_proper_fractions.append(coprime / num)

red_proper_fractions.sort()
index = red_proper_fractions.index(3 / 7)

left = red_proper_fractions[index - 1]
print(Fraction(left).limit_denominator().numerator)
# answer equals 428570