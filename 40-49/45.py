# Find the next triangle number that is 
# also pentagonal and hexagonal.

UPPER_BOUND = 100000

triangle_list = []
pentagonal_list = []
hexagonal_list = []

for i in range (1, UPPER_BOUND):
    triangle_list.append(i*(i + 1) / 2)
    pentagonal_list.append(i*(3*i - 1) / 2)
    hexagonal_list.append(i*(2*i - 1))

common = set(triangle_list).intersection(pentagonal_list, hexagonal_list)
print(common)
# answer equals 1533776805