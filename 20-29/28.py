# What is the sum of the numbers on the diagonals in a 1001 x 1001 spiral ... ?

# count represents the numbers on the diagonal of the spiral that will be
# included in diagonal_sum, diff represents the separation between diagonal
# numbers at particular spiral dimensions, i is the dimension of the spiral
diagonal_sum, count, diff, i = 1, 1, 2, 2

while (i <= 1001):
    for _ in range(4):
        count += diff
        diagonal_sum += count
    diff += 2
    i += 2

print(diagonal_sum)
# answer equals 669171001