# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Mingye He (Sunny)
# Patrick Chrisman
# Reese Lunkwitz
# Zeke Shaum

# Section: 561
# Assignment: Lab: Topic 2 (Individual)
# Date:29/08/2023

import numpy as np
#Part 1
# Assigning the variable need from linear interpolation
x1 = 10 # mins (time)
x2 = 55 # mins

y1 = 2027 #km (past houston)
y2 = 23027 #km

#Let x be any value between x1 and x2
#Assigning x a time between 10 and 55
x = 25
#Let y be the unknown y value that we seek

#formula for linear interpolation. Output is y (km past Houston)
y = (y2-y1)/(x2-x1)*(x-x1)+y1

print("Part 1:")
#printing the (y) km past houston, at the given time (x)
print("For t =", x, "minutes,the position p =", y,"kilometers")

# If x was a assigned a value outside of 11 and 55, then the program was produce an error message. 

#Part 2
# x1 = 0
# y1 = 0
circumference = 2*np.pi*6745

# Let x be the time when we want to know the km past houston
x = 300

y = (y2-y1)/(x2-x1)*(x-x1)+y1
dist_houston = y % circumference
print()
print("Part 2:")
print("For t =", x, "minutes ,the position p =", dist_houston)