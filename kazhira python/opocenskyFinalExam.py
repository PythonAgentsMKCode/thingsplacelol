#opocenskyFinalExam.py
#by Treyton Opocensky
#a module to analyze given integers

def intro():
    print()
    print("This program takes a list of numbers that you")
    print("want to analyze, and tells you the highest number,")
    print("the lowest number, the numbers in their original,")
    print("and the numbers in descending order.")
    print()

def inputNumbers():
    theList = []
    newItem = ""
    G = "G"
    #This loop adds new numbers, returns errors for non-numbers, and stops when told "G"
    while True:
        try:
            newItem = eval(input('Please enter a number ("G" to end): '))
            if newItem == "G":
                break
            theList.append(newItem)
        except:
            print("Please try that one again.")
    print()
    return theList

def printList(theList):
    for i in range(len(theList)):
        print(theList[i])
    print()

def analyzeNums(theList):
    #This loop swaps numbers so the lower always goes to the left, but it has to happen so many times to make sure
    #that even if the lowest number is on the far left, and the highest on the far right, they still swap enough
    #times to get to the other side.
    for i in range(len(theList)-1):
        for i in range(len(theList)-1):
            if theList[i] < theList[i+1]:
                theList[i],theList[i+1] = theList[i+1],theList[i]
    print("The lowest number is", theList[len(theList)-1])
    print("The highest number is", theList[0])
    print()
    return theList

def main():
    intro()
    theList = inputNumbers()
    printList(theList)
    theList = analyzeNums(theList)
    printList(theList)
    
main()
