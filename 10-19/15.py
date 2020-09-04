# How many such routes are there (from top left corner to bottom right corner, 
# moving only right and down) through a 20×20 grid?

''' Intuitionally and geometrically, the number of routes through a square
grid can be understood using Pascal's Triangle (albeit 'tilted'). The answer 
is equivalent to C(2n, n) where n is the dimension of the square grid. '''

from math import comb

n = 20
print(comb(2*n, n))
# answer equals 137846528820

