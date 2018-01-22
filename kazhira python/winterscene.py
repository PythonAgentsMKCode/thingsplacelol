#winterscene.py
#a program to display a winter scene with a Christmas tree and a snowman
#by Treyton Opocensky

from graphics import *

def tree(win):

    tt = Rectangle(Point(45,75),Point(55,150))
    tt.setFill('brown')
    tt.draw(win)
    t5 = Polygon(Point(50,90),Point(25,140),Point(75,140))
    t5.setFill('green')
    t5.draw(win)
    t4 = Polygon(Point(50,80),Point(25,125),Point(75,125))
    t4.setFill('green')
    t4.draw(win)
    t3 = Polygon(Point(50,70),Point(25,110),Point(75,110))
    t3.setFill('green')
    t3.draw(win)
    t2 = Polygon(Point(50,60),Point(25,95),Point(75,95))
    t2.setFill('green')
    t2.draw(win)
    t1 = Polygon(Point(50,50),Point(25,80),Point(75,80))
    t1.setFill('green')
    t1.draw(win)

def snowman(win):
    
    c3 = Circle(Point(150,130),25)
    c3.setFill('white')
    c3.draw(win)
    c2 = Circle(Point(150,105),20)
    c2.setFill('white')
    c2.draw(win)
    c1 = Circle(Point(150,85),15)
    c1.setFill('white')
    c1.draw(win)
    e1 = Point(145,80)
    e1.draw(win)
    e2 = Point(155,80)
    e2.draw(win)
    n = Circle(Point(150,85),3)
    n.setFill('orange')
    n.draw(win)

def main():
    win = GraphWin("Winter Scene", 200, 200)
    tree(win)
    snowman(win)

main()
