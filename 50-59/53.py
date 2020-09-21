# How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are 
# greater than one-million?

from math import comb

comb_values = 0
for n in range (23, 101):
    for r in range(n + 1):
        if (comb(n, r) > 1000000):
            comb_values += 1

print(comb_values)
# answer equals 4075