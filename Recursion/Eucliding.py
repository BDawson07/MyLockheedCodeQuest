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
#sys.path.append('D:\\CodeQuest')
#import inputs
#inputs.init("inputs")
####
def eucliding(num1:int,num2:int) -> int:

    
    difference = num2-num1
    print(f"{num2}-{num1}={difference}")

    if num1 == num2 and num2 == 1:
        print("COPRIME")
        return 0
    elif num1 == num2 and num2 != 0:
        print("NOT COPRIME")
        return 0

    nums = sorted([difference,num1])
    eucliding(nums[0],nums[1])


#input
cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
#cases = int(inputs.input())   #Test Line

for case in range(cases):
    
    nums = sys.stdin.readline().rstrip().split(",") ##IMPORANT: UNCOMMENT AFTER TESTING
    
    #nums = inputs.input() # Test Line
    nums = sorted([int(nums[0]),int(nums[1])])

    eucliding(nums[0],nums[1])
    