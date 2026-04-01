a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

det = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / det
y = (a1 * c2 - a2 * c1) / det

print("{0:.3f} {1:.3f}".format(x, y))