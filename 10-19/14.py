# Which starting number, under one million, produces the longest Collatz sequence?

def collatz(n):
    count = 1
    while (n != 1):
        if n in seq.keys():
            return count + (seq.get(n) - 1)
        elif (n % 2 == 0):
            n //= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    
    return count

seq = {}
max_count = 0
max_i = 0
for i in range(1, 1000000):
    seq_length = collatz(i)
    seq.update({i: seq_length})
    if (seq_length > max_count):
        max_count = seq_length
        max_i = i

print(max_i, max_count)
# answer equals 837799
