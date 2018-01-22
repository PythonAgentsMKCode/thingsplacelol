#month.py
#a program to print the abbreviation of a month
#by Treyton Opocensky

def month():
    months = "JanFebMarAprMayJunJulAugSepOctNovDev"
    n = int(input("Enter a number between 1 and 12: "))
    print(months[0+3*(n-1):3+3*(n-1)])

def grade():
    grades = "FFDCBA"
    n = int(input("Enter the number of correct questions"))
    print(grades[n])

grade()
