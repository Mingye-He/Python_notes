# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Mingye He (Sunny)

# Section: 561
# Assignment: Lab: Topic 3 Activity #2 (Individual)
# Date:05/06/2023

from math import*

side = float(input("Please enter the side length:"))

def area_triangle():
    area_t = sqrt(3)/4*(side)**2
    return area_t

print(f'A triangle with side {side:.2f} has area {area_triangle():.3f}')

def area_square():
    area_s = (side)**2
    return area_s
print(f'A square with side {side:.2f} has area {area_square():.3f}')

def area_pentagon():
    area_p = (1/4)*sqrt(5*(5+2*sqrt(5)))*pow(side,2)
    return area_p

print(f'A pentagon with side {side:.2f} has area {area_pentagon():.3f}')

def area_dodecagon():
    area_d = 3*(2+sqrt(3))*pow(side,2)
    return area_d

print(f'A dodecagon with side {side:.2f} has area {area_dodecagon():.3f}')