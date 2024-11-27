"""
Date: 25-10-2024
Name: Fibbinachi sequence
Description: return the fibbinachi number of a specificed integer
"""

#Neccicary libraries for all solutions
import sys
import math
import string

"""
#fibbinachi sequence:



First value is 0
2nd value is 1
3rd value is 0 + 1 = 1
4th value is 1 + 1 = 2
5th value is 1 + 2 = 3
6th value is 2+3 = 5
7th value is 3+5 = 8
8th value is 8+5 = 13



"""
def fibbinachi(limit, itter = 1, numbers = [0,0]) -> int:

    if itter == 1:
        pass
    elif itter == 2:
        numbers[1] = 1
    elif itter == 3:
        numbers = [0,1]
    else:
        numbers[0], numbers[1] = numbers[1], (numbers[1] + numbers[0])
    if itter == limit:
        return numbers[1] + numbers[0]
    
    else:
        itter += 1
        return fibbinachi(limit,itter,numbers)
    



#input
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    number = int(sys.stdin.readline().rstrip())
    print(f"{number} = {fibbinachi(number)}")