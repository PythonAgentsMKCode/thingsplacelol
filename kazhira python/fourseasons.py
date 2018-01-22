#fourseasons.py
#a module to display a tree in each seasons
#Treyton Opocensky

from graphics import *

def main():
    win = GraphWin()
    leaves = Polygon(Point(100,25),Point(50,75),Point(150,75))
    leaves.setFill("yellow")
    leaves.draw(win)
    trunk = Rectangle(Point(90,75),Point(110,125))
    trunk.setFill("brown")
    trunk.draw(win)
    change1 = win.getMouse()
    change1 = leaves.setFill("red")
    change2 = win.getMouse()
    change2 = leaves.setFill("white")
    change3 = win.getMouse()
    change3 = leaves.setFill("green")
    
main()
