#homework5-1.py
#a module to determine the artist of a portrait
#by Treyton Opocensky

from graphics import *

def loadImage():

    imageNames = ["DaVinci1","DaVinci2","DaVinci3",
                  "Rembrandt1","Rembrandt2","Rembrandt3"]
    outfile = open("trainingData.txt","w",encoding="utf8")
    textOut = ""
    for img in range(len(imageNames)):
        testImage = Image(Point(200,250), str(imageNames[img]) + str(".gif"))

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

        textOut += imageNames[img] + " " + avgRed + " " + avgGreen + " " + avgBlue + " " + avgBrightness + "\n"

    print(textOut,file=outfile)
    outfile.close()
    
loadImage()
