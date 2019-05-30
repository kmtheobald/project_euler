# sum of all multiples of 3 or 5 below a given positive integer

def multiple(n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    
    return sum

def main():
    num = int(input())
    print('Your sum is ' + str(multiple(num)))

if __name__ == "__main__":
    main()
