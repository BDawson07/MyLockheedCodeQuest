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

#input
cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
#cases = int(inputs.input())   #Test Line

for case in range(cases):
    days = []
    
    num_days = int(sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    #num_days = int(inputs.input())
    
    
    for i in range(num_days):
        #dayValues = inputs.input() # Test Line
        dayValues = sys.stdin.readline().rstrip() ##IMPORANT: UNCOMMENT AFTER TESTING
        

        days.append(list(dayValues.split(","))) 
    
    A = 0
    D = num_days
    I = .18
    P = 12
    total = 0
    for i in days:
        
        try:
             total += float(i[1])
            
        except:
            pass

        try:
            total -= float(i[2])
        except:
            pass

        A += total

    print(f"{(A/D) * (I/P):.2f}")

