# By starting at the top of the triangle below and moving to adjacent 
# numbers on the row below ... Find the maximum total from top to 
# bottom of the [given] triangle

triangle = open('triangle.txt', 'r')
lines = triangle.read().splitlines()
triangle.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        if (j == 0):
            lines[i][j] += lines[i - 1][j]
        elif (i == j):
            lines[i][j] += lines[i - 1][j - 1]
        else:
            lines[i][j] += max(lines[i - 1][j - 1], lines[i - 1][j])
        
print(max(lines[-1]))
# answer equals 7273