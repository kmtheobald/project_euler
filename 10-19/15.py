# How many such routes are there (from top left corner to bottom right corner, 
# moving only right and down) through a 20×20 grid?

''' Intuitionally and geometrically, the number of routes through a square
grid can be understood using Pascal's Triangle (albeit in a 'tilted' fashion). 
The answer is equivalent to C(2n, n), n being the dimension of the grid. '''

from math import comb

n = 20
print(comb(2*n, n))
# answer equals 137846528820

