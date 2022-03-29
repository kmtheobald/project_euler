from math import prod

# returns a list or dictionary of the prime factors for a given number n
def factorize(n, type=list):
    basis, next_prime = [2, 3, 5, 7], 11
    basis_product = prod(basis)

    factors = []
    for prime in basis:
        while (n % prime == 0):
            factors.append(prime)
            n /= prime

    init_len = basis_product + next_prime + 1
    sieve = [i for i in range(1, init_len)]
    for prime in basis:
        for num in range(2 * prime, init_len, prime):
            if num in sieve:
                sieve.remove(num)

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
    
    if (type == list):
        return factors
    elif (type == dict):
        factors_dict = {}
        unique_factors = set(factors)
        for factor in unique_factors:
            factors_dict.update({factor: factors.count(factor)})
        
        return factors_dict
    else:
        return "Invalid return type."

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def totient(num):
    prime_factors = factorize(num, dict).keys()
    for p in prime_factors:
        num *= 1 - (1 / p)
    return int(num)