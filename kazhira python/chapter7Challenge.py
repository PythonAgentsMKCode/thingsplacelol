#chapter7Challenge
#a primitive voting machine
#by Treyton Opocensky

def voteMachine():
    birthDate = input("Please enter your date of birth (mm/dd/yyyy) ")
    inputPin = input("Please enter your registration pin (8 digits) ")
    todayDate = input("Please input today's date (mm/dd/yyyy) ")
    birthDateL = birthDate.split("/")
    todayDateL = todayDate.split("/")
    birthMonth, birthDay, birthYear = int(birthDateL[0]), int(birthDateL[1]), int(birthDateL[2])
    thisYear = int(todayDateL[2])
    realPin = str(int(birthMonth)*2) + str(int(birthDay)*2) + str(int(birthYear)*2)
    print(realPin)
    if thisYear > birthYear+18:
        print("This person is eligible!")
    #elif month
    #elif elif day
    else:
        print("This person is not eligible.")

voteMachine()


#def toNumbers(strList):
#    for i in range(len(strList)):
#        strList[i] = int(strList[i])
#    return
#    
#def squareEach(nums):
#    for i in range(len(nums)):
#        nums[i] = nums[i]**2
#    return

#MAKE A DEF MAIN
