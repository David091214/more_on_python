
PI = 3.14159265


height = float(input())
radius = float(input())


volume = PI * radius ** 2 * height

area = 2 * PI * radius ** 2 + 2 * PI * radius * height

print("{0:.4f}".format(volume))
print("{0:.4f}".format(area))