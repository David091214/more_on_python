x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

A = 2 * (x2 - x1)
B = 2 * (y2 - y1)
C = x2**2 + y2**2 - x1**2 - y1**2
D = 2 * (x3 - x2)
E = 2 * (y3 - y2)
F = x3**2 + y3**2 - x2**2 - y2**2

det = A * E - B * D
x0 = (C * E - B * F) / det
y0 = (A * F - C * D) / det
r = ((x1 - x0)**2 + (y1 - y0)**2)**0.5

print("{0:.3f} {1:.3f} {2:.3f}".format(r, x0, y0))