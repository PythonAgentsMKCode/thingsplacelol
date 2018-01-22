#sevenVersusSix.py
#by Treyton Opocensky
#a module to compare the number of times 3 six and seven sided
#   die are rolled and no pairs occur

from MSDie import MSDie

def intro():
    print("This program simulates rolls of 3 seven or six")
    print("sided die, to estimate the probability of not")
    print("rolling pairs.")
    print()
    rolls = eval(input("How many rolls do you want to try? (ex. 1000) "))
    return rolls

def processRolls(rolls):
    #This section creates the dice, and sets accumulators to "0"
    six1 = MSDie(6)
    six2 = MSDie(6)
    six3 = MSDie(6)
    seven1 = MSDie(7)
    seven2 = MSDie(7)
    seven3 = MSDie(7)

    sixNoPairs = 0
    sevenNoPairs = 0

    #this loop continually rolls dice, and ticks accumulators if NO pairs are found
    for num in range(rolls):
        six1.roll()
        six2.roll()
        six3.roll()
        seven1.roll()
        seven2.roll()
        seven3.roll()

        x1 = six1.getValue()
        y1 = six2.getValue()
        z1 = six3.getValue()
        x2 = seven1.getValue()
        y2 = seven2.getValue()
        z2 = seven3.getValue()

        if x1 != y1 and x1 != z1 and y1 != z1:
            sixNoPairs += 1

        if x2 != y2 and x2 != z2 and y2 != z2:
            sevenNoPairs += 1

    return sixNoPairs, sevenNoPairs

def main():
    rolls = intro()
    sixNoPairs, sevenNoPairs = processRolls(rolls)

    #this turns the base numbers into percentages to the tenths place, and prints them with the difference
    sixPercent = int((sixNoPairs*1000)/rolls)/10
    sevenPercent = int((sevenNoPairs*1000)/rolls)/10
    print()
    print("Six sided rolls w/ no pairs:  ", sixPercent, "%")
    print("Seven sided rolls w/ no pairs:", sevenPercent, "%")
    print()
    print("The difference between six and seven is", int((sevenPercent - sixPercent)*10)/10, "%")

main()
