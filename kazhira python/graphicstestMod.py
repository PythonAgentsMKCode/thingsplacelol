#graphicstest.py
#a module to test the graphics functions of graphics.py
#by Treyton Opocensky

from graphics import *

def func1(win):
    c = Circle(Point(30,40),25)
    c.setFill('blue')
    c.setOutline('red')
    c.draw(win)

def main():
    win = GraphWin('Graphics Test', 640, 640)
    func1(win)
    
main()
