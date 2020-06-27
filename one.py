# Find the sum of all the multiples of 3 or 5 below 1000.

n, count = 1000, 0
for num in range(1, n):
    if (num % 3 == 0) or (num % 5 == 0):
            count += num

print(count)
# answer equals 233168