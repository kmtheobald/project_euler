# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import func # pylint: disable=E0401

max_totient_ratio = 1
max_num = 1
for num in range(2, 1000001):
    totient_ratio = num / func.totient(num)
    if (totient_ratio > max_totient_ratio):
        max_totient_ratio = totient_ratio
        max_num = num

print(max_num)
# answer equals 510510

