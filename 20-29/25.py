# What is the index of the first term in the Fibonacci sequence 
# to contain 1000 digits?

fib_list = [1, 1]
while(True):
    fib_next = fib_list[-1] + fib_list[-2]
    fib_list.append(fib_next)
    if (len(str(fib_next)) >= 1000):
        break

print(len(fib_list))
# answer equals 4782