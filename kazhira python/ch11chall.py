#Chapter 11 Challenge Module
#a module to create a two dimensional list
#by Treyton Opocensky


def tabbed(aList):
    for i in range(len(aList)):
        for j in range(len(aList[i])):
            print(aList[i][j], end="\t")
        print()
        
def itemSum(aList):
    iSum = 0
    for i in range(len(aList)):
        iSum += aList[i][2]
    print(iSum)

def totPrice(aList):
    price = 0
    for i in range(len(aList)):
        price += aList[i][2] * aList[i][3]
    print(price)
        
def main():
    theData = []
    theData.append([])
    theData[0].append("18347")
    theData[0].append("G2 Ink Pens, Each")
    theData[0].append(12)
    theData[0].append(2.79)
    theData.append([])
    theData[1].append("59981")
    theData[1].append("Legal Pads, Each")
    theData[1].append(12)
    theData[1].append(2.19)
    theData.append([])
    theData[2].append("83362")
    theData[2].append("Paper Clips, Small, Box")
    theData[2].append(6)
    theData[2].append(3.49)
    theData.append([])
    theData[3].append("87654")
    theData[3].append("3M Post-It Notes, Pkg")
    theData[3].append(10)
    theData[3].append(3.79)
    theData.append([])
    theData[4].append("83056")
    theData[4].append("Paper Clips, Large, Box")
    theData[4].append(2)
    theData[4].append(4.19)
    theData.append([])
    theData[5].append("90098")
    theData[5].append("Staples, Standard, Box")
    theData[5].append(8)
    theData[5].append(3.33)
    theData.append([])
    theData[6].append("42659")
    theData[6].append("Letter Opener")
    theData[6].append(1)
    theData[6].append(7.69)
    theData.append([])
    theData[7].append("93329")
    theData[7].append("Stapler, Ergonomic")
    theData[7].append(1)
    theData[7].append(9.99)
    theData.append([])
    theData[8].append("57634")
    theData[8].append("Poster Board, Assorted Colors, Pkg")
    theData[8].append(1)
    theData[8].append(17.79)

    tabbed(theData)
    itemSum(theData)
    totPrice(theData)
main()
