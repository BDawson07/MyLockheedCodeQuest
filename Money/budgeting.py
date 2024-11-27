"""
Date: 11-05-2024
Name: Are we on budget
Description: Calculate the average cost varience of n numbers
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
    
    #sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    
    #lineItems = int(inputs.input()) # Test Line
    #budgetedCost = inputs.input() #Test Line
    #actualCost = inputs.input() #Test Line

    lineItems = int(sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    budgetedCost = str(sys.stdin.readline().rstrip())
    actualCost = str(sys.stdin.readline().rstrip())
    
    budgetedCost = list(budgetedCost.split(" "))
    actualCost = list(actualCost.split(" "))
    varience = 0
    for indx in range(lineItems):
        varience += (float(actualCost[indx]) - float(budgetedCost[indx]))
    
    
    varience /= (lineItems)

    print(f"{varience:.2f}")