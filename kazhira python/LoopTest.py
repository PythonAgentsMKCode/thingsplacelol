#LoopTest.py
#by Treyton Opocensky
#a module to test loops (duh)

#sequential for
str1 = "Loop Demo"
for ch in str1:
    print(ch,end="*")
print()

#range for
for i in range(5,100,5):
    print(i,end="-")
print()

#sequential for
myList = ["one","two","three","four","five"]
for item in myList:
    print(item)
print()

#interactive while
response = "Y"
while response == "Y":
    print("Still want to play, I see!")
    response = input("Do you still want to play? (Y/N): ")
print()

#sentinel controlled while
totTemps = 0
i = 0
response = int(input("Please enter the first temperature: (999 to quit) ->"))
while response != 999:
    totTemps += response
    response = int(input("Please enter the first temperature: (999 to quit) ->"))
    i += 1
print("The average temperature was: " + str(totTemps//i))

#conditional while
age = int(input("Please enter voter age. "))
reg = input("Please enter if voter is registered. (Y/N): ")
while age > 17 and reg == "Y":
    print("You would have voted.")
    age = int(input("Please enter voter age. "))
    reg = input("Please enter if voter is registered. (Y/N): ")
print("Uh oh. Something went wrong.")
