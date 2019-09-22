# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def self_powers(n):
    modulo = 10**10
    sum = 0
    for i in range(1, n + 1):
        sum += i**i
        sum = sum % modulo

    return sum

def main():
    num = int(input())
    print(self_powers(num)) 

if __name__ == "__main__":
    main()

# for input of 1000, sum = 9110846700