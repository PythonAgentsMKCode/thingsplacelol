# rectangle.py
# a program to draw and measure the area and perimeter of a triangle
# Treyton Opocensky

from graphics import *

def main():
    win = GraphWin()
    message = Text(Point(100,5),"Click on two points.")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    rect = Rectangle(p1,p2)
    rect.setFill("green")
    rect.setOutline("Red")
    rect.draw(win)
    length = abs(p2.getX() - p1.getX())
    height = abs(p2.getY() - p1.getY())
    print("The area of the rectangle is " + str(length * height) + ".")
    print("The perimeter of the rectangle is " + str(2*length+2*height) + ".")

main()
