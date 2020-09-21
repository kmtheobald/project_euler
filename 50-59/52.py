# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.

x = 1
while(True):
    a, b, c, d, e = 2*x, 3*x, 4*x, 5*x, 6*x

    a = list(str(a))
    b = list(str(b))
    c = list(str(c))
    d = list(str(d))
    e = list(str(e))
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    
    if (a == b == c == d == e):
        break
    else:
        x += 1

print(x)
# answer equals 142857