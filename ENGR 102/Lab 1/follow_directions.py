# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Sunny He (Mingye He)
# Section: 
# Assignment: Lab: Topic 1 (Activity #3)
# Date: 24/8/2023

import numpy as np
print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x = 1")
print("My guess on is 0")
print( )

x = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]

for value in x:
    result = np.sin(value - 1) / (value - 1)
    print(result)

print( )
# Printing out a my guess
print("My guess was a little off.")
    
    
