# Given that L is the length of the wire, for how many values of 
# L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

from math import gcd
from collections import Counter
import copy

primitive_triples = []
for i in range(2, 1000):
    coprime_list = [k for k in range(1, i) if gcd(i, k) == 1]
    for coprime in coprime_list:
        x = i**2 - coprime**2
        y = 2*i*coprime
        z = i**2 + coprime**2
        if ((bool(i % 2 == 0) != bool(coprime % 2 == 0)) and (x + y + z) < 1500000):
            primitive_triples.append(x + y + z)

triples = copy.deepcopy(primitive_triples)
for triple in primitive_triples:
    n = 2
    while (n * triple < 1500000):
        triples.append(n * triple)
        n += 1

unique = 0
count = Counter(triples)
for size in count:
    if count[size] == 1:
        unique += 1

print(unique)
# answer equals 161667

