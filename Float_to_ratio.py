from fractions import Fraction

N= float(input())

frac = Fraction(N).limit_denominator()
numerator = frac.numerator
denominator = frac.denominator

print(f"{numerator}/{denominator}")