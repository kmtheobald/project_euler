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

routes = [bin(num)[2:].zfill(15) for num in range(2**14)]

sums = []
for route in routes:
    index, total = 0, 0
    for i in range(len(lines)):
        if (route[i] == '1'):
            index += 1
            total += lines[i][index]
        else:
            total += lines[i][index]
    sums.append(total)

print(max(sums))
# answer equals 1074