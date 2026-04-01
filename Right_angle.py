# import math
# a = int(input())
# b = int(input())

# if (a>b):
#     c = (a**2) + (b**2) 
#     print(math.sqrt(c))
# elif (b>a):
#     temp = b
#     b = a
#     a = temp
#     c = (a**2) + (b**2)
#     print(math.sqrt(c))
# else :
#     print("non")
from math import sqrt, fabs

a=int(input())
b=int(input())
c=int(sqrt(a*a+b*b))
c2 = int(sqrt(fabs((a*a-b*b))))

if a*a+b*b == c*c and a+b>c and b+c>a and a+c>b:
    print ("c")

elif fabs(a*a-b*b)==c2*c2 and a+b>c2 and b+c2>a and a+c2>b:
    if c2 == min(a,b,c2):
        print("a")
    else:
        print("b")
else:
    print("non")