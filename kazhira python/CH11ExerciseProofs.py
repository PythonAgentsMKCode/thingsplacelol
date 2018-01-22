#CH11ExerciseProof.py
#Some functions to demonstrate Ch11 Exercise solutions

testList = [27,5,16,27,2,8,32,43,27,17]

def count(myList, x):
    numFound = 0
    
    print("First use the given count function to provide result: ")
    numFound = myList.count(x)
    print("The number found was",numFound)
    
    numFound = 0
    print("Now for my count function to provide result: ")
    for item in myList:
        if item==x:
            numFound += 1
    print("The number found was",numFound)
            
#count(testList,27)

def isin(myList, x):
    isFound = False
    
    print("First use the 'x in myList' expression to provide result: ")
    ifFound = x in myList
    print("The number",x,"was found:",ifFound)
    
    ifFound = False
    print("Now for my isin function to provide result: ")
    for item in myList:
        if item==x:
            isFound = True
            break
    print("The number",x,"was found:",isFound)
            
#isin(testList,27)
#isin(testList,99)

def index(myList, x):
    iFound = -1
    
    print("First use the given index function to provide result: ")
    iFound = myList.index(x)
    print("The number",x,"was found at",iFound)
    
    iFound = -1
    print("Now for my index function to provide result: ")
    for i in range(len(myList)):
        if myList[i]==x:
            iFound = i
            break
    print("The number",x,"was found at",iFound)
            
#index(testList,8)

def reverse(myList):

    tempL = []
    print("Now for my reverse function to provide result: ")
    for i in range(len(myList)-1,-1,-1):
        tempL.append(myList[i])
    for item in tempL:
        print(item,end=" ")
    print()

    tempL = myList    
    print("First use the given reverse function to provide result: ")
    tempL.reverse()
    for item in tempL:
        print(item,end=" ")
    print()
    
#I had to evoke these two reversals in the opposite order than the others.
#WHY?
#reverse(testList)

def sort(myList,useProvided):
    
    if useProvided == True:
        tempL = myList 
        print("First use the given sort function to provide result: ")
        tempL.sort()
        for item in tempL:
            print(item,end=" ")
        print()

        return
  
    tempL = myList 
    print("Now use my sort algorithm to provide result: ")
    for i in range(len(tempL)):
        for j in range(len(tempL)-1):
            if tempL[j]>tempL[j+1]:
                tempL[j], tempL[j+1] = tempL[j+1], tempL[j]
    for item in tempL:
        print(item,end=" ")
    print()
   
#sort(testList, True)
#sort(testList,False)

def removeDups(myList):
    sort(myList,True)
    for i in range(len(myList)-1):
        while i<len(myList)-1 and myList[i]==myList[i+1]:
            throwaway = myList.pop(i)
    for item in myList:
        print(item,end=" ")

removeDups(testList)
