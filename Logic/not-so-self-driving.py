"""
Date: 12/24/2024
Name: Not so self driving
Description: take a number, then take that number of inputs, then 
use a logic gate to either produce BRAKE, SWERVE, or SAFE
"""

#Neccicary libraries for all solutions
import sys
import math
import string




#recall number of activities
cases = int(sys.stdin.readline().rstrip())


#take that number of inputs
for case in range(cases):
    speed, obj_distance  = sys.stdin.readline().rstrip().split(":")
    speed, obj_distance = float(speed), float(obj_distance)
    

    #IMPORTANT: Remeber to handle Zero Division Errors
    try:
        1/speed
    except ZeroDivisionError:
        print("SAFE")
        continue

    #if car is projected to hit in one second or less print "SWERVE" 
    if obj_distance / speed <= 1:
        print("SWERVE")
    #elif car is projected to hit in five  second or less print "BRAKE"
    elif obj_distance / speed <= 5:
        print("BRAKE")
    #else car is safe print "SAFE"
    else:
        print("SAFE")