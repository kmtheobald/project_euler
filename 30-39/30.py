# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits.

pent = []
for num in range(2, 400000):
    digits = [int(char) for char in str(num)]
    total = 0
    for digit in digits:
        total += pow(digit, 5)
    
    if (total == num):
        pent.append(num)

print(sum(pent))
# answer equals 443839