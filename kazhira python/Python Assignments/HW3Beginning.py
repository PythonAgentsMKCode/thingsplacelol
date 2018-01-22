#hw3.py
# a program to create an ignore list and look for frequencies in text files
# by Brian Kokensparger


def getText():

    infile = open("novelTest.txt","r")

    allText = infile.read()

    return allText

def inspectWord(theWord,wList,fList,ignoreList,iList):
    tempWord = theWord.rstrip("\"\'.,`;:-!?")
    tempWord = tempWord.lstrip("\"\'.,`;:-!")
    tempWord = tempWord.lower()
    if tempWord in ignoreList:
        iList.append(tempWord)  
    elif tempWord in wList:
          tIndex = wList.index(tempWord)
          fList[tIndex]+=1
    else:
          wList.append(tempWord)
          fList.append(1)

def printParallelLists(wList,fList):
    for i in range(len(wList)):
        if fList[i] > 50:
            print(wList[i],fList[i])

def main():
    wList = []
    fList = []
    ignoreList = ["a","the","is","that","was","in","to","it","with","of",
                  "and","for","as","they","this","i","it's","are","had","my",
                  "no","on","or","at","so","those","these","us","did","her",
                  "she","he","by","its","has","him","if","while","about",
                  "from","very","also","what","do","you","your","will","an",
                  "we","were","can","who","not","be","their","but","will",
                  "into","use","when","his","them","which","there","own",
                  "one","after","have","all",""]
    iList = []
    
    myText = getText()
    myWords = myText.split(" ")

    for word in myWords:
        inspectWord(word,wList,fList,ignoreList,iList)
    
    #print(myText)
    printParallelLists(wList,fList)
        
main()
    
