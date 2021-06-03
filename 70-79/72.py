# How many elements would be contained in the set of reduced 
# proper fractions for d ≤ 1,000,000?

import func # pylint: disable=E0401

LIMIT = 1000000
totient_sum = 0
for num in range(2, LIMIT + 1):
    totient_sum += func.totient(num)

print(int(totient_sum))
# answer equals 303963552391

