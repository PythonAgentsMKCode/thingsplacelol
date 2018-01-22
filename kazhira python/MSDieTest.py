#MSDieTest.py
#a file to test the MSDie class

from MSDie import MSDie

def printValues(obj,n):
    print("Sides:",obj.getSides(),
          "; Roll value:",obj.getValue(),
          "; n:",n)

myDie = MSDie(10)
printValues(myDie,0)
n = myDie.getValue()
printValues(myDie,n)
myDie.setValue(7)
printValues(myDie,n)
myDie.roll()
printValues(myDie,n)
myDie.setValue(3)
printValues(myDie,n)
n= myDie.getValue()
printValues(myDie,n)
myDie = MSDie(n)
printValues(myDie,n)
