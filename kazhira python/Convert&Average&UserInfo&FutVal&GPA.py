#convert&average&welcome&futval&findGPA.py
#a program to convert celcius to farenheit, average 2 or 3 numbers, calculate accumulated interest, and find GPA with welcome

def welcome():
    print("Welcome to my program!")
    print("This program can:")
    print()
    print("Convert Celcius to Farenheit with ''convert()''")
    print("Average two numbers with ''average2()''")
    print("Average three numbers with ''average3()''")
    print("Display info with ''userInfo()''")
    print("Calculate accumulated interest with 'futVal()'")
    print("Calculate accumulated credit hours with 'findGPA'")
    print()
    print("Enjoy!")

welcome()

def convert():
    celcius = eval(input("What is the Celcius Temperature? "))
    farenheit = 9/5 * celcius + 32
    print("The temperature is", farenheit, "degrees Farenheit")

def average():
    print("Add the quantity of numbers you would like to average to the end of the word.")

def average2():
    X = eval(input("What is the first number you want to average? "))
    Y = eval(input("What is the second number you want to average? "))
    average2 = ( X + Y ) / 2
    print(average2)

def average3():
    X = eval(input("What is the first number you want to average? "))
    Y = eval(input("What is the second number you want to average? "))
    Z = eval(input("What is the third number you want to average? "))
    average3 = ( X + Y + Z ) / 3
    print(average3)

def userInfo():
    A = eval(input("What is your address? (ex. 3012) "))
    B = (input("What is your street name? (ex. Cass Street) "))
    C = eval(input("True or Flase, does an active student live there? (ex. True) "))
    print(A, B, C)

def futVal():
    print("This program calculates the future value of")
    print("an investment after a number of years.")
    print()
    principal = eval(input("Enter the initial principal (ex. 10000): "))
    apr = eval(input("Enter the annual interest rate (ex. 0.05): "))
    X = eval(input("Enter how many years the interest will accumulate over (ex. 10): "))
    for i in range(X):
        principal = principal * (1 + apr)
    print("The value in", X, "years is", principal)

def findGPA():
    print("This program will tell you how many credit hours you attain for 5 classes of three credit hours each.")
    course1 = (input("What is the name of your first class? (ex. CSC 221) "))
    letter1 = (input("What letter grade did you recieve in this course? (ex. A or B+) "))
    points1 = eval(input("How many points are associated with that grade? (ex. 4 for A or 3.5 for B+) "))
    course2 = (input("What is the name of your second class? (ex. CSC 221) "))
    letter2 = (input("What letter grade did you recieve in this course? (ex. A or B+) "))
    points2 = eval(input("How many points are associated with that grade? (ex. 4 for A or 3.5 for B+) "))
    course3 = (input("What is the name of your third class? (ex. CSC 221) "))
    letter3 = (input("What letter grade did you recieve in this course? (ex. A or B+) "))
    points3 = eval(input("How many points are associated with that grade? (ex. 4 for A or 3.5 for B+) "))
    course4 = (input("What is the name of your fourth class? (ex. CSC 221) "))
    letter4 = (input("What letter grade did you recieve in this course? (ex. A or B+) "))
    points4 = eval(input("How many points are associated with that grade? (ex. 4 for A or 3.5 for B+) "))
    course5 = (input("What is the name of your fifth class? (ex. CSC 221) "))
    letter5 = (input("What letter grade did you recieve in this course? (ex. A or B+) "))
    points5 = eval(input("How many points are associated with that grade? (ex. 4 for A or 3.5 for B+) "))
    
    hours1 = 3 * points1
    hours2 = 3 * points2
    hours3 = 3 * points3
    hours4 = 3 * points4
    hours5 = 3 * points5
    
    GPA = hours1 + hours2 + hours3 + hours4 + hours5

    print("Your GPA for the semester is", GPA / 15, "!")
    




    
