#Math.py
#Treyton Opocensky
#A file to test multiple mathematical equations

def main():
    print("This program tests multiple mathematical equations. You can use...")
    print("aR() to find the area of a given rectangle.")
    print("aC() to find the area of a given circle.")
    print()
    
main()

def aR():
    lR = eval(input("What is the length of the rectangle? "))
    bR = eval(input("What is the width of the rectangle? "))
    aR = lR * bR
    print()
    print("The area of the rectange is", aR)

def aC():
    import math
    rC = eval(input("What is the radius of the circle? "))
    aC = math.pi * ( rC ** 2 )
    print("The area of the circle is", aC)
