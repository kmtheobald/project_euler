# How many n-digit positive integers exist which are also an nth power?

n, i = 1, 1

nth_power_integers = []
while (True):
    if (len(str(i**n)) == n):
        nth_power_integers.append(i**n)
    i += 1
    
    if (len(str(i**n)) > n):
        n += 1
        i = 1
    if (i == 9 and len(str(i**n)) < n):
        break

print(len(nth_power_integers))
# answer equals 49