from fractions import Fraction
num1 = int(input())
den1= int(input())

num2 = int(input())
den2 = int(input())

F1 = Fraction(num1,den1)
F2 = Fraction(num2,den2)

print(f"({num1}/{den1})+({num2}/{den2})={(F1)+(F2)}")
print(f"({num1}/{den1})-({num2}/{den2})={(F1)-(F2)}")
print(f"({num1}/{den1})*({num2}/{den2})={(F1)*(F2)}")
print(f"({num1}/{den1})/({num2}/{den2})={(F1)/(F2)}")





