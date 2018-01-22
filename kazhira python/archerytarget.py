#archerytarget.py
#a module to display an archery target
#by Treyton Opocensky

from graphics import *

def target(win):
    
    c5 = Circle(Point(100,100),75)
    c5.draw(win)
    c5.setFill('white')
    c4 = Circle(Point(100,100),60)
    c4.draw(win)
    c4.setFill('black')
    c3 = Circle(Point(100,100),45)
    c3.draw(win)
    c3.setFill('blue')
    c2 = Circle(Point(100,100),30)
    c2.draw(win)
    c2.setFill('red')
    c1 = Circle(Point(100,100),15)
    c1.draw(win)
    c1.setFill('yellow')
    
def main():
    win = GraphWin("Archery Target", 200, 200)
    target(win)

main()
