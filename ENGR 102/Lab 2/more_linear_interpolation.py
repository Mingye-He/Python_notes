# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Sunny He (Mingye He)
# Section: 
# Assignment: Lab: Topic 2 (Activity #3)
# Date: 24/8/2023

x0 = 8 #meters
y0 = 6 # m
z0 = 7 # m
t0 = 12 # in Sec


x2 = -5 #m
y2 = 30 #m
z2 = 9 #m
t2 = 85 #sec



# Let t be the time that is requested between 8 and 85 mins
t= 30

# Writing down the x, y, and z linear interpolation formula
x = (x2-x0)/(t2-t0)*(t-t0)+ x0
y = (y2-y0)/(t2-t0)*(t-t0) + y0
z = (z2-z0)/(t2-t0)*(t-t0) + z0

print("At time 30.0 seconds:")
print("x1 = ", x, "m")
print("y1 = ", y, "m")
print("z1 = ", z, "m")
print("-----------------------")


t = 37.5

x = (x2-x0)/(t2-t0)*(t-t0)+ x0
y = (y2-y0)/(t2-t0)*(t-t0) + y0
z = (z2-z0)/(t2-t0)*(t-t0) + z0


print("At time 37.5 seconds:")
print("x2 = ", x, "m")
print("y2 = ", y, "m")
print("z2 = ", z, "m")

print("-----------------------")


t = 45
x = (x2-x0)/(t2-t0)*(t-t0)+ x0
y = (y2-y0)/(t2-t0)*(t-t0) + y0
z = (z2-z0)/(t2-t0)*(t-t0) + z0
print("At time 45.0 seconds:")
print("x3 = ", x, "m")
print("y3 = ", y, "m")
print("z3 = ", z, "m")
print("-----------------------")
t = 52.5 
x = (x2-x0)/(t2-t0)*(t-t0)+ x0
y = (y2-y0)/(t2-t0)*(t-t0) + y0
z = (z2-z0)/(t2-t0)*(t-t0) + z0
print("At time 52.5 seconds:")
print("x4 = ", x, "m")
print("y4 = ", y, "m")
print("z4 = ", z, "m")

print("-----------------------")
t = 60.0
x = (x2-x0)/(t2-t0)*(t-t0)+ x0
y = (y2-y0)/(t2-t0)*(t-t0) + y0
z = (z2-z0)/(t2-t0)*(t-t0) + z0
print("At time 60.0 seconds:")
print("x5 = ", x, "m")
print("y5 = ", y, "m")
print("z5 = ", z, "m")