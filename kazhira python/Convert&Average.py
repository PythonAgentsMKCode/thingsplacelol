#convert&average&welcome.py
#a program to convert celcius to farenheit and average 2 or 3 numbers with welcome

def welcome():
    print("Welcome to my program!")
    print("This program can:")
    print()
    print("Convert Celcius to Farenheit with ''convert()''")
    print("Average two numbers with ''average2()''")
    print("Average three numbers with ''average3()''")
    print("Display info with ''userInfo()''")
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
    B = eval(input("What is your street name? (in quotes) "))
    C = eval(input("True or Flase, does an active student live there? (ex. True) "))
    print(A, B, C)
