# Find the first four consecutive integers to have four distinct prime 
# factors each. What is the first of these numbers?

from func import factorize # pylint: disable=E0401

count = 0
four_prime_factors = []
for num in range(650, 200000):
    if (len(factorize(num)) == 4):
        count += 1
        four_prime_factors.append(num)
        if (count == 4):
            break
        continue
    else:
        count = 0
        four_prime_factors.clear()

print(four_prime_factors[0])
# answer equals 134043

