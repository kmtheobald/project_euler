# adding even Fibonacci terms below a given positive integer

def fibonacci(n):
    list = [1, 2]
    while ((list[-1] + list[-2]) < n):
        list.append(list[-1] + list[-2])
    return list

def sum_terms(list):
    sum = 0
    for x in range(1, len(list), 3):
        sum += list[x]
    return sum

def main():
    num = int(input())
    print('Your sum is ' + str(sum_terms(fibonacci(num))))

if __name__ == "__main__":
    main()       