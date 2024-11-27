"""
Date: 24-10-2024
Name: AEIOU
Description: take a string and determine the number of vowels in the string
"""

#Neccicary libraries for all solutions
import sys
import math
import string

#input
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    count = 0
    string = sys.stdin.readline().rstrip()
    for letter in string:
        
        if letter.upper() in ["A","E","I","O","U"]:
            count += 1
    print(count)