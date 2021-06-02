# How many different ways can one hundred be written as a sum of 
# at least two positive integers?

SUM = 100
numbers = [num for num in range(1, 100)]
def num_ways(total, current):
    if total == 0:
        return 1
    if total < 1:
        return 0

    ways = 0
    for i in range(current, -1, -1):
        ways += num_ways(total - numbers[i], i)
    return ways

print(num_ways(SUM, 98))
# answer equals 190569291

