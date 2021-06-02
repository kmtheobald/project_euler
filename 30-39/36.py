# Find the sum of all numbers, less than one million, which are palindromic 
# in base 10 and base 2.

import func # pylint: disable=E0401

double_palindromes = []
for num in range(1, 1000000):
    num_bin = bin(num)[2:]
    if (func.is_palindrome(num) and \
        func.is_palindrome(num_bin)):
        double_palindromes.append(num)

print(sum(double_palindromes))
# answer equals 872187

