# What is the 10 001st prime number?

import math

prime_list = [2]
integer = 3
while (len(prime_list) < 10001):
    comp = False
    for prime in prime_list:
        if (prime > math.sqrt(integer)):
            break
        if ((integer % prime == 0)):
            comp = True
            break
    if (not comp):
        prime_list.append(integer)
    integer += 2

print(prime_list[-1])