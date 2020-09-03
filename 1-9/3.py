# What is the largest prime factor of the number 600851475143 ?

from math import prod

n = 600851475143
basis, next_prime = [2, 3, 5, 7], 11
basis_product = prod(basis)

init_len = basis_product + next_prime + 1
sieve = [i for i in range(1, init_len)]
for prime in basis:
    for num in range(2 * prime, init_len, prime):
        if num in sieve:
            sieve.remove(num)

factors = []
for prime in basis:
    while (n % prime == 0):
        factors.append(prime)
        n /= prime

inc = []
for i in range(len(basis) + 1, len(sieve) - 1):
    diff = sieve[i + 1] - sieve[i]
    inc.append(diff)

i = 0
while (pow(next_prime, 2) <= n):
    if (n % next_prime == 0):
        factors.append(next_prime)
        n /= next_prime
    else:
        next_prime += inc[i]
        i = (i + 1) if (i < (len(inc) - 1)) else 0

if (n > 1):
    factors.append(int(n))
print(max(factors))
# answer equals 6857