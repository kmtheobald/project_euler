# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

import decimal
from math import sqrt

decimal.getcontext().prec = 105 # safely above 100 to avoid rounding errors
digital_sum = 0
for i in range(1, 101):
    root = decimal.Decimal(i).sqrt()
    string = list(str(root))
    if (len(string) > 2):
        del string[1]
        num_list = [int(c) for c in string]
        digital_sum += sum(num_list[:100])
    else:
        continue

print(digital_sum)
# answer equals 40886
