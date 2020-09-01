# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def square_diff(n):
    sum_square = 0
    for i in range(1, (n + 1)):
        sum_square += i**2
    
    square_sum = ((n * (n + 1)) // 2)**2
    return (square_sum - sum_square)

def main():
    num = int(input())
    print(square_diff(num))

if __name__ == "__main__":
    main()

# input of 100 yields 25164150