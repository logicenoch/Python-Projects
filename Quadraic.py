import math as mat
"""
An implementation of the 
Quadraic general formula or equation.
"""

# Takes the values from the user and assign it to the variables
a, b, c = [int(x) for x in input(
    "Enter the coefficients of the equation (a,b,c): ").split()]

# Calclates the Descriminant of the equation
D = b**2 - 4*a*c

# Solves the equation for the following conditions
# 1 - If D > 0.
# 2 - If D < 0.
# 3 - If D = 0.

if D == 0:
    print("Nature Of Roots: Equal and Real")
    x1 = (-b + mat.sqrt(D)) / 2 * a
    x2 = (-b - mat.sqrt(D)) / 2 * a
    print(f"x1: {x1} - x2: {x2}")

elif D > 0:
    print("Nature Of Roots: Unequal and Real")
    x1 = (-b + mat.sqrt(D)) / 2 * a
    x2 = (-b - mat.sqrt(D)) / 2 * a
    print(f"x1: {x1} - x2: {x2}")

else:
    print("Nature Of Roots: Complex roots")
    real_part = f"{(-b) / (2 * a)}"
    complex_part = f"i{(mat.sqrt(-D)) / (2*a)}"
    x1 = real_part + "+" + complex_part
    x2 = real_part + "-" + complex_part
    print(f"x1: {x1} - x2: {x2}")
