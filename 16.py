# What is the sum of the digits of the number 2^1000?

num = pow(2, 1000)
num_list = [int(i) for i in str(num)]
print(sum(num_list))
# answer equals 1366