"""
Date: 04-11-2024
Name: Animal Farm
Description: Take 3 numbers. One is turkies, one is goats, one is horses. multiply by number of legs and add
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

#input
cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
#cases = int(inputs.input())   #Test Line

for case in range(cases):
    
    nums = sys.stdin.readline().rstrip() ##IMPORANT: UNCOMMENT AFTER TESTING
    
    #nums = inputs.input() # Test Line
    num1,num2,num3 = nums.split(" ")
    
    num1 = int(num1)*2
    num2 = int(num2)*4
    num3 = int(num3)*4
    print(num1+num2+num3)