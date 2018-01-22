#chapter7Challenge
#a primitive voting machine
#by Treyton Opocensky

def voteMachine():
    dob = input("Please enter your date of birth (mm/dd/yyyy) ")
    pin = input("Please enter your registration pin (8 digits) ")
    don = input("Please input today's date (mm/dd/yyyy) ")
    yob = dob[6,10]
    yon = don[6,10]
    print(yob, yon)
