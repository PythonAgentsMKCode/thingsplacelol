#calculate.py
#A program to calculate thing.

def main():
    print("This program calculates the average of 5 numbers.")
    print()
    A = eval(input("What is the first number you want to average? "))
    B = eval(input("What is the second number you want to average? "))
    C = eval(input("What is the third number you want to average? "))
    D = eval(input("What is the fourth number you want to average? "))
    E = eval(input("What is the fifth number you want to average? "))
    average = (A + B + C + D + E) / 5
    print("The average is", average)

main()
