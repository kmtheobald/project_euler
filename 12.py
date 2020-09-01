# What is the value of the first triangle number to have over 
# five hundred divisors?

import math

def triangle_value(n):
    return (n * (n + 1)) // 2

def num_divisors(n):
    count = 0
    m = math.floor((math.sqrt(n)))
    for i in range(1, m + 1):
        if (n % i == 0):
            if (n == i**2):
                count += 1
            else:
                count += 2
    return count

for integer in range(1, 100000):
    tri_val = triangle_value(integer)
    if (num_divisors(tri_val) > 500):
        print(integer, tri_val) # triangle number = 76576500 for int 12375
        break