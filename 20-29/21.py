# Evaluate the sum of all the amicable numbers under 10000.

from func import factorize

proper_divisors_dict = {}
for i in range(1, 10000):
    factor_dict = factorize(i)
    sum_proper_divisors = 1
    for factor in factor_dict:
        value_count = factor_dict.get(factor)
        sum_proper_divisors *= ((pow(factor, value_count + 1) - 1) / (factor - 1))

    sum_proper_divisors -= i
    proper_divisors_dict.update({i: int(sum_proper_divisors)})

proper_divisors_dict = {key: value for key, value in proper_divisors_dict.items() if value != 1}

amicable_numbers = []
for key, value in proper_divisors_dict.items():
    if (key != value and proper_divisors_dict.get(value) == key):
        amicable_numbers.append(key)

print(sum(amicable_numbers))
# answer equals 31626

