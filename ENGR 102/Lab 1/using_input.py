# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Sunny He (Mingye He)
# Section: 
# Assignment: Lab: Topic 3 (Activity #1)
# Date: 24/8/2023s

from math import*

# A) Calculating Force
# Printing a statement that
# print("This program calculates the applied force give mass and acceleration")
# m = float(input("Please enter the mass (kg):"))
# a = float(input("Please enter the acceleration (m/s^2):"))
#
# def force():
#     n = m * a
#     return n
#
# print(f'Force is {force()} N')

# B) Wavelength
print("This program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm):"))
theta = float(input("Please enter the angle (degrees):"))
def wavelength():
    rad = radians(theta)
    w = 2 * d * sin(rad)
    return w


print(f'Wavelength is {wavelength()} nm')

# C) Radioactive Decay
print("This program calculates the how much Radon-222 is left given time and initial amount")
t = input("Please enter the time (days):")
int_amount = input("Please enter the initial amount ")
h = 3.8
def gram():
    g = int_amount* pow(2, -1*t/h))
    return g
print(f'Radon-222 left is {gram()},g')
# print("Radon-222 left is ",int_amt*2**(-1*t/h), "g")

# D) Pressure
print("This program calculates the pressure given moles, volume, and temperature")
mol = float(input("Please enter the number of moles:"))
v = float(input("Please enter the volume (m^3):"))
temp = float(input("Please enter the temperature (K):"))
r = 8.314 #gas constant

def pressure():
    p = mol*temp*r/v/1000
    return p
print(f'Pressure is {pressure()} kPa')

