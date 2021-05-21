# How many distinct terms are in the sequence generated 
# by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

powers = []
for i in range(2, 101):
    for j in range(2, 101):
        powers.append(pow(i, j))

print(len(set(powers)))
# answer equals 9183