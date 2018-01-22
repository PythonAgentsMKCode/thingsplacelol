#OpocenskyChange.py
#Treyton Opocensky
#This program calculates the average number of burial permits issued throughout 7 years.

def main():
    print("This program calculates the average number of burial")
    print("permits issued throughout 7 years.")
    print()
    year1 = input("What is the first year you wish to enter into the calculation? (ex. 2017) ")
    permits1 = eval(input("How many permits were issued during that year? (ex. 25) "))
    year2 = input("What is the second year you wish to enter into the calculation? ")
    permits2 = eval(input("How many permits were issued during that year? "))
    year3 = input("What is the third year you wish to enter into the calculation? ")
    permits3 = eval(input("How many permits were issued during that year? "))
    year4 = input("What is the fourth year you wish to enter into the calculation? ")
    permits4 = eval(input("How many permits were issued during that year? "))
    year5 = input("What is the fifth year you wish to enter into the calculation? ")
    permits5 = eval(input("How many permits were issued during that year? "))
    year6 = input("What is the sixth year you wish to enter into the calculation? ")
    permits6 = eval(input("How many permits were issued during that year? "))
    year7 = input("What is the seventh year you wish to enter into the calculation? ")
    permits7 = eval(input("How many permits were issued during that year? "))

    print()
    print(year1 , permits1)
    print(year2 , permits2)
    print(year3 , permits3)
    print(year4 , permits4)
    print(year5 , permits5)
    print(year6 , permits6)
    print(year7 , permits7)
    print()
    print("The average number of permits issued a year is", ( permits1 + permits2 + permits3 + permits4 + permits5 + permits6 + permits7 ) / 7 )

main()
