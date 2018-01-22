#homework_3.py
#a program to list the occurances of important words in a text
#by Treyton Opocensky


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
    outfile = open("wordOut.txt","w")
    for i in range(len(wList)):
        if fList[i] > 75:
            print(wList[i],fList[i],file=outfile)

def main():
    wList = []
    fList = []

    ignoreList = ["","the","of","and","a","to","in","is","you","that","it",
                  "he","was","for","on","are","as","with","his","they","i",
                  "at","be","this","have","from","or","one","had","by","word",
                  "but","not","what","all","were","we","when","your","can","said",
                  "there","use","an","each","which","she","do","how","their","if",
                  "will","up","other","about","out","many","then","them","these","so",
                  "some","her","would","make","like","him","into","time","has","look",
                  "two","more","write","go","see","number","no","way","could","people",
                  "my","than","first","water","been","call","who","oil","its","now",
                  "find","long","down","day","did","get","come","made","may","part",]

    iList = []

    myText = getText()
    myWords = myText.split(" ")

    for word in myWords:
        inspectWord(word,wList,fList,ignoreList,iList)
    
    printParallelLists(wList,fList)
    
main()
    
