"""
Date: 24-10-2024
Name: Addiply
Description: takes 2 numbers, prints their sum, then prints their product
"""

#Neccicary libraries for all solutions
import sys
import math
import string



cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    int1, int2 = sys.stdin.readline().rstrip().split(" ")
    int1, int2 = int(int1), int(int2)

    #calculations    
    sum = int1 + int2
    product = int1 * int2
    
    #final output
    print(f"{sum} {product}")