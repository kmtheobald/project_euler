# Find the sum of all the positive integers which cannot be written as the 
# sum of two abundant numbers.

from func import factorize

UPPER_LIMIT = 28123

def sum_of_proper_divisors(num):
    total = 1
    factors_dict = factorize(num)
    for factor in factors_dict:
        total *= (pow(factor, factors_dict.get(factor) + 1) - 1) // (factor - 1)
    return (total - num)

abundant = []
for i in range(1, UPPER_LIMIT + 1):
    divisor_sum = sum_of_proper_divisors(i)
    if (divisor_sum > i):
        abundant.append(i)

abundant_sums = []
length = len(abundant)
for i in range(length):
    for j in range(i, length):
        current_sum = abundant[i] + abundant[j]
        if (current_sum > UPPER_LIMIT):
            break
        else:
            abundant_sums.append(abundant[i] + abundant[j])

nonabundant = []
for i in range(1, UPPER_LIMIT + 1):
    if i not in abundant_sums:
        nonabundant.append(i)

print(sum(nonabundant))
# answer equals 4179871