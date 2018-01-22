#graphicstest.py
#a module to test the graphics functions of graphics.py
#by Treyton Opocensky

from graphics import *

def func1(win):
    c = Circle(Point(30,40),25)
    c.setFill('blue')
    c.setOutline('red')
    c.draw(win)

def func2(win):
    r = Rectangle(Point(20,20),Point(40,40))
    r.setFill(color_rgb(0,255,150))
    r.setWidth(3)
    r.draw(win)

def func3(win):
    l = Line(Point(100,000),Point(100,200))
    l.setOutline('red4')
    l.setArrow('first')
    l.draw(win)

def func4(win):
    Oval(Point(50,50),Point(60,100)).draw(win)

def func5(win):
    shape = Polygon(Point(5,5),Point(50,50),
                Point(5,50), Point(50,5))
    shape.setFill('orange')
    shape.draw(win)

def func6(win):
    t = Text(Point(100,100),"Hello World!")
    t.setFace("courier")
    t.setSize(16)
    t.setStyle("italic")
    t.draw(win)
    
def main():
    win = GraphWin('Graphics Test', 640, 640)
    func1(win)
    func2(win)
    func3(win)
    func4(win)
    func5(win)
    func6(win)
    
main()
