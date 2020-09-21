# ... Find the last ten digits of this prime number.

modulus = 10**10
base = 28433

for _ in range(7830457):
    base *= 2
    if (base > modulus):
        base %= modulus
base += 1

print(base)
# answer equals 8739992577