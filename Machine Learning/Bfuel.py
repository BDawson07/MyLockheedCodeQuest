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
    ratios = {
        
    }    
    #info = str(sys.stdin.readline().rstrip()).split(" ") ##IMPORANT: UNCOMMENT AFTER TESTING
    pass
    info = str(inputs.input()).split(" ") # Test Line
    fuel = int(info[0])
    tankNum = int(info[1])


    tanks = str(inputs.input())
    factor = 1
    tankLimits = [int(i) for i in list(tanks.split(" "))]

    for i in range(len(tankLimits)):
        ratios[i] = {
            "fill": 0,
            "ratio":1,
            "full":False
        }


    while fuel > 0:
        factor = len(tankLimits)
        fuel *= factor

        for i in range(len(tankLimits)):
            tankLimits[i] *= factor
            if not ratios[i]["full"]:

                if ratios[i]["full"] + fuel >= tankLimits[i]:
                    ratios[i]["fill"] =  ratios[i]["fill"]* factor + tankLimits[i]-ratios[i]["fill"]
                    ratios[i]["ratio"] = ratios[i]["ratio"]
                    print(ratios)

        break











"""
    info = str(inputs.input()).split(" ") # Test Line
    fuel = int(info[0])
    tankNum = int(info[1])

    tankFill = [0 for i in range(tankNum)]
    print(tankFill)
    print("once")

    tanks = str(inputs.input())
    factor = 1
    tankLimits = [int(i) for i in list(tanks.split(" "))]

    while fuel > 0:
        factor *= tankNum
        fill = fuel*tankNum
        
        fuel = 0
        
        for indx,obj in enumerate(tankLimits):
            if tankFill[indx] + fill >= obj*factor:
                tankFill[indx] = tankLimits[indx]*factor
                print(tankFill)
                tankLimits
                tankNum -= 1
                fuel += fill - obj*factor   
                print(f"factor: {factor}")
            else:
                tankFill[indx] += fill
            print(fuel)
                


        
    



"""