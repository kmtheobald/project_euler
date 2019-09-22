# By considering the terms of the Fibonacci below four million, 
# find the sum of the even-valued terms.

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
    print(sum_terms(fibonacci(num)))

if __name__ == "__main__":
    main()

# Input of 4000000 yields 4613732