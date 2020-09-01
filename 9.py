# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

for m in range(1, 30):
    for n in range(1, m):
        if (m*(m + n) == 500):
            # print(m, n)
            print((m**2 - n**2) * 2*m*n * (m**2 + n**2))
