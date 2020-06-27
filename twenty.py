# Find the sum of the digits in the number 100!
from math import factorial

n = factorial(100)
num_list = list(str(n))
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
print(sum(num_list))
# answer equals 648

m, total = factorial(100), 0
while (m > 0):
    total += (m % 10)
    m = (m // 10)
print(total)
# answer equals 648