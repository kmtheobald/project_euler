# What is the first value which can be written as the sum of primes in 
# over five thousand different ways?

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, \
                59, 61, 67, 71, 73, 79, 83, 89, 97]
def num_ways(total, current):
    if total == 0:
        return 1
    if total < 1:
        return 0

    ways = 0
    for i in range(current, -1, -1):
        ways += num_ways(total - prime_list[i], i)
    return ways

for val in range(1, 200):
    if (num_ways(val, len(prime_list) - 1) > 5000):
        print(val)
        break
# answer equals 71