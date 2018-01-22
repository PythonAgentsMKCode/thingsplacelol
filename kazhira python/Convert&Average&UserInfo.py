#convert&average&welcome&futval.py
#a program to convert celcius to farenheit, average 2 or 3 numbers, and calculate accumulated interest with welcome

def welcome():
    print("Welcome to my program!")
    print("This program can:")
    print()
    print("Convert Celcius to Farenheit with ''convert()''")
    print("Average two numbers with ''average2()''")
    print("Average three numbers with ''average3()''")
    print("Display info with ''userInfo()''")
    print("Calculate accumulated interest with 'futVal()'")
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
