# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

abc = 0
for b in range(1, 30):
    for a in range(1, b):
        if (b * (b + a) == 500):
            abc = (b**2 - a**2) * 2*b*a * (b**2 + a**2)
            break

print(abc)
# answer equals 31875000
