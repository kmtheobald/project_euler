# How many different ways can £2 be made using any number of coins?

SUM = 200
pence = [1, 2, 5, 10, 20, 50, 100, 200]
def num_ways(total, current):
    if total == 0:
        return 1
    if total < 1:
        return 0
    
    ways = 0
    for i in range(current, -1, -1):
        ways += num_ways(total - pence[i], i)
    return ways

print(num_ways(SUM, 7))
# answer equals 73682