# By considering the terms of the Fibonacci below four million, 
# find the sum of the even-valued terms.

n = 4000000
fib_seq = [1, 2]
while ((fib_seq[-1] + fib_seq[-2]) < n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

count = 0
for even_term in range(1, len(fib_seq), 3):
    count += fib_seq[even_term]
print(count)
# answer equals 4613732