#fuel

import math

def exercise8_6():
    theNumber = 0
    
    while theNumber < 3:
        theNumber = eval(input("Please enter the number to check for prime: "))

    theNumber = math.floor(theNumber)
    topval = math.ceil(math.sqrt(theNumber))

    for i in range(2, theNumber):
        if theNumber%i == 0:
            print("The number", theNumber, "is not prime.")
            return
    print("The number", theNumber, "is prime.")

def exercise8_10():
    prevReading = 0
    miles = 0
    gallons = 0

    infile = open("tripLegs.txt","r")

    text=infile.readline()

    while text != "":
        tempList = text.split(" ")
        tempList[0] = eval(templist[0])
        tempList[1] = eval(templist[1])
        if prevReading != 0:
            miles += tempList[0] - prevReading
        gallons += tempList[1]
        print(prevReading, tempList[0],tempList[1]







exercise8_6()
