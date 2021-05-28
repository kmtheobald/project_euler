# Find the sum of all numbers which are equal to the sum of 
# the factorial of their digits.

from math import factorial
UPPER_BOUND = 2500000

curious = []
for num in range(3, UPPER_BOUND):
    digit_list = [int(i) for i in str(num)]
    total = 0
    for digit in digit_list:
        total += factorial(digit)
    if (num == total):
        curious.append(num)

print(sum(curious))
# answer equals 40730