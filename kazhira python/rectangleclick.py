#rectangleclick.py
#A program to change colors of rectangles upon mouse click
#Treyton Opoensky

from graphics import *

def main():
    win = GraphWin()
    rl = Rectangle(Point(25,50),Point(75,75))
    rl.setFill("green")
    rl.draw(win)
    rr = Rectangle(Point(125,50),Point(175,75))
    rr.setFill("blue")
    rr.draw(win)

    colorswap = win.getMouse()
    colorswap = rl.setFill("blue")
    colorswap = rr.setFill("green")
    
main()
