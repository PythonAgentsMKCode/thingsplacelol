#opocenskyRectangle.py
#Treyton Opocensky
#A python module to calculate important coordinates of a rectangle

def main():
    print("This module calculates coordinates of a rectangle.")
    print()
    print("Enter the x and y coordinates of the top")
    x1,y2 = eval(input("left corner (in the format 'x,y'): "))
    dx  = eval(input("How wide is the rectangle (must be positive integer): "))
    dy  = eval(input("How tall is the rectangle (must be positive integer): "))
    print()
    x2 = x1 + dx
    y2 = y1 - dy
    xc = x1 + dx // 2
    yc = y1 - dy // 2
    print("The points of the rectangle are as follows.")
    print("Top left:      (" + str(x1) + "," + str(y1) + ")")
    print("Top right:     (" + str(x2) + "," + str(y1) + ")")
    print("Bottom left:   (" + str(x1) + "," + str(y2) + ")")
    print("Bottom right:  (" + str(x2) + "," + str(y2) + ")")
    print("Center:        (" + str(xc) + "," + str(yc) + ")")

main()
