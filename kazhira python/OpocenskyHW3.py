# homeWork3.py
# a module to...
# by Treyton Opocensky

def inspectWord(theWord,wList,fList):
    tempWord = theWord.rstrip("\"\'.,`;:-!")
    tempWord = tempWord.lstrip("\"\'.,`;:-!")
    tempWord = tempWord.lower()
    if tempWord in wList:
          tIndex = wList.index(tempWord)
          fList[tIndex]+=1
    else:
          wList.append(tempWord)
          fList.append(1)
