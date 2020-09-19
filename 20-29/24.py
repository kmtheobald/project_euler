# What is the millionth lexicographic permutation of the 
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

lex_permutations = list(permutations('0123456789'))
millionth = int(''.join(list(lex_permutations[999999])))

print(millionth)
