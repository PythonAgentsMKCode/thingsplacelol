#homework5-2.py
#a module to determine the artist of a portrait
#by Treyton Opocensky

from graphics import *

def testImage():

    newImages = ["mystery1","mystery2","mystery3"]
    mysteryList = []

    for img in range(len(newImages)):

        if img == 0:
            guess = input("Who do you think painted the first mystery image? (DaVinci, or Remrandt) ")
        if img == 1:
            guess = input("Who do you think painted the second mystery image? (DaVinci, or Remrandt) ")
        if img == 2:
            guess = input("Who do you think painted the third mystery image? (DaVinci, or Remrandt) ")
        
        testImage = Image(Point(200,250), str(newImages[img]) + str(".gif"))
        theWidth = testImage.getWidth()
        theHeight = testImage.getHeight()
        totRed = 0
        totGreen = 0
        totBlue = 0
        totBrightness = 0
        totPixel = 0

        for i in range(theWidth):
            for j in range(theHeight):
                r,g,b = testImage.getPixel(i,j)
                brightness = int(round(0.299*r + 0.587*g + 0.114*b))
                totRed += r
                totGreen += g
                totBlue += b
                totBrightness += brightness
                totPixel += 1
                
        avgRed = round(totRed / totPixel)
        avgGreen = round(totGreen / totPixel)
        avgBlue = round(totBlue / totPixel)
        avgBrightness = round(totBrightness / totPixel)

        avgRed = str(avgRed)
        avgGreen = str(avgGreen)
        avgBlue = str(avgBlue)
        avgBrightness = str(avgBrightness)
        
        mysteryList.append([])
        mysteryList[img].append(newImages[img])
        mysteryList[img].append(avgRed)
        mysteryList[img].append(avgGreen)
        mysteryList[img].append(avgBlue)
        mysteryList[img].append(avgBrightness)

        difference = 1000000
        differenceIndex = -1

        infile = open("trainingData.txt","r",encoding="utf8")

        for x in range(6):
            text = infile.readline()
            knownStats = text.split(" ")

            tempRedDiff = abs((int(knownStats[1]) - int(mysteryList[img][1])) / int(mysteryList[img][1]))
            tempGreenDiff = abs((int(knownStats[2]) - int(mysteryList[img][2])) / int(mysteryList[img][1]))
            tempBlueDiff = abs((int(knownStats[3]) - int(mysteryList[img][3])) / int(mysteryList[img][1]))
            tempBrightnessDiff = abs((int(knownStats[4]) - int(mysteryList[img][4])) / int(mysteryList[img][1]))

            tempDifference = tempRedDiff + tempGreenDiff + tempBlueDiff + tempBrightnessDiff

            if tempDifference < difference:
                difference = tempDifference
                differenceIndex = knownStats[0]

        if differenceIndex[0] == "D":
            if guess.lower() == "davinci":
                print("Your guess was correct!")
            if guess.lower() != "davinci":
                print("Your guess was incorrect.")
        if differenceIndex[0] == "R":
            if guess.lower() == "rembrandt":
                print("Your guess was correct!")
            if guess.lower() != "rembrandt":
                print("Your guess was incorrect.")
                
        print()        
        print("The closeset painting to", mysteryList[img][0], "is", differenceIndex, ".")
        print()
                   
testImage()
