"""
Date: 31-10-2007
Name: Aerospace Intruders
Description: Take a number of ships, and engage them in order

<ShipName> xLoc: <x>
"""

#Neccicary libraries for all solutions
import sys
import math
import string
"""

inputs = [
"SHIP1_A:150,150",
"SHIP2_B:200,150",
"SHIP3_C:165,130",
"SHIP4_A:205,135",
"SHIP5_B:155,105",
"SHIP6_C:195,120",
"SHIP7_A:140,50",
"SHIP8_B:175,70",
"SHIP9_C:215,70",
"SHIP10_A:145,10",
"SHIP11_B:160,30",
"SHIP12_C:185,35",
"SHIP13_C:225,20"
]


def input():
    i = inputs[0]
    inputs.remove(i)
    return i
"""
#input
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    num_ships = int(sys.stdin.readline().rstrip())
    
    ships = []
    for i in range(num_ships):
        ship = sys.stdin.readline().rstrip()
        two_parts = ship.split(":")
        ship_name, ship_class = two_parts[0].split("_")
        ship_x, ship_y = two_parts[1].split(",")
        ships.append([ship_name, ship_class, int(ship_x), int(ship_y), None])      #[name, class, x, y, xLoc]
    
    
    while len(ships) > 0:
        new_values = []  
        for i in ships:                 #Will be at prediction:
            if i[1] == "A":
                speed = 10


        
            elif i[1] == "B":
                speed = 20
        
            elif i[1] == "C":
                speed = 30

            i[4] = i[2]          #xLoc location
            i[2] -= speed        #predicted location
            
            for indx,obj in enumerate(new_values):
                #print(i,obj)
                
                
                if int(i[4]) == int(obj[4]):    #handaling ties, gets rid of the bigger y value
                    #print("tie")
                    #print(i,obj)
                    if i[3] > obj[3]:
                        new_values.insert(indx,i)
                        break
    
                elif i[4] <= obj[4]:                      #attacks the value with the lowest x value
                    new_values.insert(indx,i)
                    break
            else:
                new_values.append(i)
            #print(new_values)
        
        print(f"Destroyed Ship: {new_values[0][0]} xLoc: {new_values[0][4]}")
        ships.remove(new_values[0])
