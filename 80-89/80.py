# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

import decimal
from math import sqrt

decimal.getcontext().prec = 101
digital_sum = 0
for i in range(1, 101):
    root = decimal.Decimal(i).sqrt()
    num_list = list(str(root))
    del num_list[:2]
    dec_list = [int(x) for x in num_list]
    digital_sum += sum(dec_list)

print(digital_sum)
# answer doesn't equal 40308? or 40752?