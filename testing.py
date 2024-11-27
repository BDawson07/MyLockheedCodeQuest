import math
def rounding(number:float, digits=2, zeros=False):
    
    number = [i for i in str(number)]
    counter = 0
    count = False
    newNumber = []
    intlen = 00
    for indx,obj in enumerate(number):
        if obj == ".":
            intlen = indx
            count = True

        elif count:
            counter += 1
            
        if counter == digits:    #when you reach the proper digits
            if int(number[indx+1]) >= 5:   #if it rounds up
                if int(obj) != 9:
                    newNumber[indx] = str(int(obj) + 1)
                else:
                    newNumber[indx-1] = str(int(obj) - 1)
                    newNumber[indx] = "0"
            else:  #if it rounds down nothing happens
                pass
            break
        else:
            newNumber[indx] = obj

    print(newNumber)



print(rounding(3.4))