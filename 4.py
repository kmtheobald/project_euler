# Find the largest palindromic number made from the product of 
# two 3-digit numbers.

def is_palindrome(num):
    int_list = [int(i) for i in str(num)]
    for i in range((len(int_list) // 2) + 1):
        if int_list[i] != int_list[-(i + 1)]:
            return False
    return True

top_pal = []
for i in range(900, 1000):
    for j in range(900, 1000):
        product = i * j
        if (is_palindrome(product) == True):
            top_pal.append(product)

top_pal.sort()
print(top_pal[-1])
# answer equals 906609