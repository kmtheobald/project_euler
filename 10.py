# Find the sum of all the primes below two million

import math

prime_list = []
for integer in range (2, 2000000):
    comp = False
    for prime in prime_list:
        if (prime > math.sqrt(integer)):
            break
        if ((integer % prime == 0)):
            comp = True
            break
    if (not comp):
        prime_list.append(integer)

print(sum(prime_list))