# import math

# x = i(input())
# y = float(input())

# p = math.sqrt(x**2 + y**2)
# o = math.atan2(y, x)


# print(f"{p:.4f}, {o:.4f}")

from math import atan2, hypot

x = int(input())
y = int(input())

p = hypot(x,y)
o = atan2(y, x)


print(f"{p:.4f},{o:.4f}")