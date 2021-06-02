# How many Lychrel numbers are there below ten-thousand?

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import func # pylint: disable=E0401

lychrel_count = 0
for num in range(1, 10000):
    lychrel_flag = False
    for _ in range(50):
        reverse_num = int(str(num)[::-1])
        num += reverse_num
        if (func.is_palindrome(num)):
            lychrel_flag = True
            break
    if not lychrel_flag:
        lychrel_count += 1

print(lychrel_count)
# answer equals 249