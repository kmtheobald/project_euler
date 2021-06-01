# Find the value of the following expression: 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

champerowne = '0.'
for num in range(1, 200000):
    champerowne += str(num)

product = int(champerowne[2]) * int(champerowne[11]) * int(champerowne[101]) * int(champerowne[1001]) \
            * int(champerowne[10001]) * int(champerowne[100001]) * int(champerowne[1000001])

print(product)
# answer equals 210
