#exercise 11.5
#recreate myList.[count(x), isin(x), index(x), reverse, sort]

def count(myList, x):
    n = 0
    for i in range(len(myList)):
        if myList[i] == x:
            n += 1
    print(n)

def isin(myList, x):
    found = False
    for i in range(len(myList)):
        if i == x:
            found = True
    print(found)

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            print(i)
            return
        else:
            i += 1

def reverse(myList):
    temp = []
    for i in range(len(myList)-1,-1,-1):
        temp.append(myList[i])
    print(temp)

def sort(myList):
    for i in range(len(myList)):
        for j in range(len(myList)-1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    print(myList)

def main():

    myList = [0,2,4,6,1,3,5,3,2,5,3]
    '''
    count(myList, 5)
    count(myList, 18)
    print()
    isin(myList, 2)
    isin(myList, 17)
    print()
    index(myList, 5)
    index(myList, 6)
    reverse(myList)
    sort(myList)
    '''
main()
