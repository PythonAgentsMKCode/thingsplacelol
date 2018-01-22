#fuelEff.py
#by Treyton Opocensky
#a program to compute the fuel efficiency of a multi-leg journey

# get starting odometer reading and name variables

#create loop to get new odometer readings, and gas used

#print leg mpg and total mpg

def fuelEff():
    odomIniStart = eval(input("What does the odometer initially read? "))
    odomStart = odomIniStart
    gasIniStart = 0
    gasStart = gasIniStart
    odomTot = 0
    gasTot = 0
    odomNew = 1

    while odomNew > 0:
        odomNew, gasNew = eval(input("What is the new odometer reading, and how much gas was used? (odometer, gas) "))
        if odomNew > odomStart:
            print("The mpg for this leg is", (odomNew - odomStart) / (gasNew - gasStart), str("mpg"))
            odomStart = odomNew
            gasStart = gasNew
        else:
            print("Your total mpg is", (odomNew - odomIniStart) - (gasNew - gasIniStart), str("mpg"))
            return

def main():
    fuelEff()
main()
