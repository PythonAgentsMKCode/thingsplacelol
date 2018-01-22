#pizzaPrice.py
#Treyton Opocensky
#A program to calculate the cost of pizza per square inch

import math

def main():
    diam = eval(input("Please enter the diameter (in inches) of this pizza: "))
    totCost = eval(input("Please enter total cost of this pizza: "))
    sqInches = math.pi*(diam/2)**2
    print("The square inches of your pizza is: ", sqInches)
    costSqInch = totCost/sqInches
    costSqInch = math.floor(costSqInch*1000)/10
    print("The cost per square inch of your pizza is: ", costSqInch, "cents.")

main()
