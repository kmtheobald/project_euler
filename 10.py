# Find the sum of all the primes below two million

from math import sqrt

n, prime_list = 2000000, []
for integer in range (2, n):
    comp = False
    for prime in prime_list:
        if (prime > sqrt(integer)):
            break
        if ((integer % prime == 0)):
            comp = True
            break
    if (not comp):
        prime_list.append(integer)

print(sum(prime_list))
# answer equals 142913828922