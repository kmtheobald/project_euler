# For which value of p ≤ 1000, is the number of solutions maximised?

from math import gcd
from statistics import mode
import copy

primitive_triples = []
for i in range(2, 25):
    coprime_list = [k for k in range(1, i) if gcd(i, k) == 1]
    for coprime in coprime_list:
        x = i**2 - coprime**2
        y = 2*i*coprime
        z = i**2 + coprime**2
        if ((bool(i % 2 == 0) != bool(coprime % 2 == 0)) and (x + y + z) < 1000):
            primitive_triples.append(x + y + z)

triples = copy.deepcopy(primitive_triples)
for triple in primitive_triples:
    n = 2
    while (n * triple < 1000):
        triples.append(n * triple)
        n += 1

print(mode(triples))
# answer equals 840
    