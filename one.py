# Find the sum of all the multiples of 3 or 5 below 1000.

def multiple(n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    
    return sum

def main():
    num = int(input())
    print(multiple(num))

if __name__ == "__main__":
    main()

# Input of 1000 yields 233168