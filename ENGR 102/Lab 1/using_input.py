# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Sunny He (Mingye He)
# Section: 
# Assignment: Lab: Topic 3 (Activity #1)
# Date: 24/8/2023s

import numpy as np

# A) Force
# Let the variable m represent mass of the object
m = 27
# Let the variable a represent the acceleration of the object
a = 1.5
#Calculate and print the force of the object by multiplying m with a
print("Force is", m*a, "N")


# B) Wavelength
# Let d represent the distance of between crystal layers (nm)
d = 0.025
# Let theta represent the degree angle (degree)
theta = 35
# Calculating and print the length of wavelength of x-rayx)
print("Wavelength is", 2*d*np.sin(np.radians(35)),"nm")

# C) Radioactive Decay
# Let int_amt represent the initial amount of Radon 222 (grams)
int_amt = 27
# Let h represent the half life of Radon 222 (days)
h = 3.8
# Let t represent the amount of days it has been
t =5
# Calculating and printing the amount Radon 222 in a sentence
print("Radon-222 left is ",int_amt*2**(-1*t/h), "g")


# D) Pressure
# Let mol represent the moles of the ideal gas (mol)
mol = 5
# Let v represent the volume of the gas (m^3)
v = 0.27
# Let T represent the temperature in Kelvins of the gas
T = 415
#Let represent the gas constant (m^3Pa/K*mol)
r = 8.314
# Calculating the Pressure of the ideal gas
print("Pressure is", mol*T*r/v/1000,"kPa")


