x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

dx1 = x2 - x1
dy1 = y2 - y1
dx2 = x4 - x3
dy2 = y4 - y3

if dx1 * dy2 == dy1 * dx2:
    print("Yes")
else:
    print("No")