# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

MODULUS = 10**10

total = 0
for i in range(1, 1001):
    total += pow(i, i)
        
print(total % MODULUS)
# answer equals 9110846700