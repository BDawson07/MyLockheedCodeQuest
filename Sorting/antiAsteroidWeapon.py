"""
Date: 11-05-2024
Name: Anti Asteoird weapon
Description: order a list of points based on their distance from earth
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
    
    asteroidCnt = int(sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    #asteroidCnt = int(inputs.input()) # Test Line
    
    asteroids = []
    
    for asteroidCnt in range(asteroidCnt):
        #asteroid = inputs.input() # Test Line
        asteroid = sys.stdin.readline().rstrip()##IMPORANT: UNCOMMENT AFTER TESTING

        x, y = asteroid.split(" ")
        distance = math.sqrt(int(x)**2 + int(y)**2)     #Distance
        

        #list ordering
        for indx, obj in enumerate(asteroids):
            if obj[0] > distance:
                asteroids.insert(indx,[distance,x,y])  
                break
        else:
            asteroids.append([distance,x,y])

    #final output
    for i in asteroids:
        print(f"{i[1]} {i[2]}")
