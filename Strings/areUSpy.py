"""
Date: 11-4-2024
Name: Are you a spy
Description: get a greeting and response, and the alphabet in the response must match the greeting
"""

#Neccicary libraries for all solutions
import sys
import math
import string
import re

### DELETE AFTER TESING
#sys.path.append('D:\\CodeQuest')
#import inputs
#inputs.init("inputs")
####

#input
cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
#cases = int(inputs.input())   #Test Line

for case in range(cases):
    
    phrases = str(sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    #phrases = inputs.input() # Test Line

    greeting, response = phrases.split("|")
    greeting = re.sub(r'[^a-zA-Z]', '', greeting)
    response =  re.sub(r'[^a-zA-Z]', '', response)      #HELPFULL CODE SNIP
    
    greeting = [i.lower() for i in greeting]
    response = [i.lower() for i in response]
    #checks each character is in the list
    for i in response:
        if i not in greeting:

            print("You're not a secret agent!") 
            break
    else:
        print("That's my secret contact!")