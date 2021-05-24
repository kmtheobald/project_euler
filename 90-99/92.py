# How many starting numbers below ten million will arrive at 89?

def square_digit_chain(n):
    chain = [n]
    while (n != 1 and n != 89):
        split_n = [int(char) for char in str(n)]
        m = 0
        for digit in split_n:
            m += pow(digit, 2)
        chain.append(m)
        n = m
    
    if (chain[-1] == 89):
        return True 
    else:
        return False

eighty_nine = 0
for num in range(1, 10000000):
    result = square_digit_chain(num)
    if (result):
        eighty_nine += 1

print(eighty_nine)
# answer equals 8581146