"""
Date: 04-11-2024
Name: Anagram Checker 
Description: check strings to ensure they are anagrams
"""

#Neccicary libraries for all solutions
import sys
import math
import string
import sys

#sys.path.append('D:\\CodeQuest')
#import inputs
#inputs.init("inputs")


#input
cases = int(sys.stdin.readline().rstrip())
#cases = int(inputs.input())   #Test Line

for case in range(cases):
    word1, word2 = str(sys.stdin.readline().rstrip()).split("|")
    
    #word1, word2 = str(inputs.input()).split("|") # Test Line


    lword1 = [i for i in word1]
    lword2 = [i for i in word2]
    
    #check for same wqord
    if word1 == word2:
        print(f"{word1}|{word2} = NOT AN ANAGRAM")
    else:
        lword1.sort()
        lword2.sort()
        if lword1 == lword2:

            print(f"{word1}|{word2} = ANAGRAM")
        else:
            print(f"{word1}|{word2} = NOT AN ANAGRAM")
