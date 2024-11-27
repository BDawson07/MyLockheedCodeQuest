"""
Date: DD-MM-YY
Name: 
Description:
"""

#Neccicary libraries for all solutions
import sys
import math
import string

### DELETE AFTER TESING
sys.path.append('D:\\CodeQuest')
import inputs
inputs.init("inputs")
####

#input
#cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
cases = int(inputs.input())   #Test Line

for case in range(cases):
    
    #sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    
    planes = inputs.input() # Test Line
    for i in range(int(planes)):

        name = inputs.input()
        coords = inputs.input()
        px,py = coords.split(",")
        landing = inputs.input()

        slx,sly = landing.split(",")  #start of runway
        landing = inputs.input()
        elx,ely = landing.split(",")   #end of runway


        slope1 = -(int(py)-int(sly))/(int(px)-int(slx))
        slope2 = -(int(py)-int(ely))/(int(px)-int(elx))

        print(slope1, slope2)
        if (0.8 <= slope1 <= 1.6) and (0.8 <= slope2 <= 1.6) :
            print(f"{name}, Clear To Land!")
        else:
            print(f"{name}, Abort Landing!")