import math
h = int(input("enter the height of the ladder in meters "))
angle = int(input("enter the angle of the ladder in degree "))
if angle <= 0 or angle >= 90:
    print("invalid entry")
else:
    rad = math.radians(angle)
    L = h/math.sin(rad)
    print (str(L) , "meters")