a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

det = a * e - b * d
x = (e * c - f * b) / det
y = (a * f - c * d) / det

print(f"{x:.3f} {y:.3f}")