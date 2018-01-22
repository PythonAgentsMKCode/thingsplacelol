#CH8ExerciseProof.py
#Some functions to demonstrate Ch8 Exercise solutions

import math

def exercise8_6():
    theNumber = 0

    while theNumber<3:
        theNumber = eval(input("Please enter the number to check for prime: "))
    
    theNumber = math.floor(theNumber)
    topVal = math.ceil(math.sqrt(theNumber))

    for i in range(2,theNumber):
        if theNumber%i == 0:
            print("The number",theNumber,"is not prime.")
            return
    print("The number", theNumber, "is prime.")

#exercise8_6()


def exercise8_10():
    prevReading = 0
    miles = 0
    gallons = 0

    infile = open("tripLegs.txt","r")

    text=infile.readline()

    while text!="":
        tempList = text.split(" ")
        tempList[0]=eval(tempList[0])
        tempList[1]=eval(tempList[1])
        if prevReading !=0:
            miles += tempList[0]-prevReading
        gallons += tempList[1]
        print(prevReading,tempList[0],tempList[1],miles,gallons)
        if prevReading != 0:
            print("The mpg for this leg of the trip is",(tempList[0]-prevReading)/tempList[1],".")
        prevReading = tempList[0]
        text=infile.readline()

    print()
    print("The mpg for the entire trip is",miles/gallons,".")

    infile.close()
    
#exercise8_10()

from graphics import *

def loadImage():
    win = GraphWin("Test Image", 400, 500)
    testImage = Image(Point(200,250), "Leonardo-Da-Vinci.gif")
    testImage.draw(win)
    throwAway = win.getMouse()
    win2 = GraphWin("Grayed Image", 400, 500)
    newImage = Image(Point(200,250),400,500)
    theWidth = testImage.getWidth()
    theHeight = testImage.getHeight()
    for i in range(0,theWidth):
        for j in range(0,theHeight):
            r,g,b = testImage.getPixel(i,j)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            newImage.setPixel(i,j,color_rgb(brightness, brightness, brightness))
    newImage.draw(win2)
    oFileName = input("Please enter output file name (end with .gif): ")
    newImage.save(oFileName)
  

loadImage()
            
