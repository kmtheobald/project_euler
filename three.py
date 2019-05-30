# the largest prime factor of a given positive integer

def prime_factor(n):
    list = [2]
    for x in range(3, (n // 2) + 1, 2):
        composite = 0
        for y in list:
            if x % y == 0:
                composite = 1
                break
        if (composite == 0):
            list.append(x)
    print(list)
    return list

def factor_check(factors, n):
    for x in reversed(factors):
        if n % x == 0:
            return x

def main():
    num = int(input())
    print(factor_check(prime_factor(num), num))

if __name__ == "__main__":
    main()