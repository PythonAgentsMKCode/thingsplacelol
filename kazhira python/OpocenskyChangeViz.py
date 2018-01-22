#ChangeViz.py
#a module to visualize purchased burial plots over a period of time
#by Treyton Opocensky

from graphics import *

def main():
    win = GraphWin("Cemetary Visualization",720,400)
    s0 = Rectangle(Point(3,3),Point(717,357))
    s0.setWidth(3)
    s0.setFill("white")
    s0.draw(win)
    s1 = Rectangle(Point(10,190),Point(250,350))
    s1.setFill("white")
    s1.draw(win)
    s2 = Rectangle(Point(10,10),Point(250,170))
    s2.setFill("white")
    s2.draw(win)
    t1 = Polygon(Point(275,190),Point(445,190),Point(275,345))
    t1.setFill("white")
    t1.draw(win)
    t2 = Polygon(Point(280,350),Point(455,195),Point(455,350))
    t2.setFill("white")
    t2.draw(win)
    t3 = Polygon(Point(480,195),Point(480,350),Point(675,350))
    t3.setFill("white")
    t3.draw(win)
    t4 = Polygon(Point(485,190),Point(685,190),Point(685,350))
    t4.setFill("white")
    t4.draw(win)
    t5 = Polygon(Point(485,170),Point(685,170),Point(685,15))
    t5.setFill("white")
    t5.draw(win)
    t6 = Polygon(Point(480,10),Point(480,165),Point(680,10))
    t6.setFill("white")
    t6.draw(win)
    t7 = Polygon(Point(280,10),Point(455,10),Point(455,165))
    t7.setFill("white")
    t7.draw(win)
    t8 = Polygon(Point(275,15),Point(275,165),Point(440,165))
    t8.setFill("white")
    t8.draw(win)
    s4 = Rectangle(Point(3,357),Point(717,397))
    s4.setWidth(3)
    s4.setFill("white")
    s4.draw(win)
    year0 = Text(Point(360,380),"Please click the mouse.")
    year0.setFace("courier")
    year0.setSize(16)
    year0.setStyle("italic")
    year0.draw(win)

    win.getMouse() #year 1 (1872)
    s1.setFill(color_rgb(255,230,255))
    s2.setFill(color_rgb(255,255,255))
    t1.setFill(color_rgb(255,179,255))
    t2.setFill(color_rgb(255,179,255))
    t3.setFill(color_rgb(255,230,255))
    t4.setFill(color_rgb(255,230,255))
    t5.setFill(color_rgb(255,255,255))
    t6.setFill(color_rgb(255,255,255))
    t7.setFill(color_rgb(128,000,128))
    t8.setFill(color_rgb(255,179,255))
    year0.setFill("white")
    year1 = Text(Point(360,380),"1872")
    year1.setFace("courier")
    year1.setSize(16)
    year1.setStyle("italic")
    year1.draw(win)

    win.getMouse() #year 2 (1873)
    s1.setFill(color_rgb(255,230,255))
    s2.setFill(color_rgb(255,255,255))
    t1.setFill(color_rgb(255,128,255))
    t2.setFill(color_rgb(255,128,255))
    t3.setFill(color_rgb(255,179,255))
    t4.setFill(color_rgb(255,230,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(230,000,230))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(255,128,255))
    year1.setFill("white")
    year2 = Text(Point(360,380),"1873")
    year2.setFace("courier")
    year2.setSize(16)
    year2.setStyle("italic")
    year2.draw(win)

    win.getMouse() #year 3 (1874)
    s1.setFill(color_rgb(255,230,255))
    s2.setFill(color_rgb(255,255,255))
    t1.setFill(color_rgb(255,77,255))
    t2.setFill(color_rgb(255,77,255))
    t3.setFill(color_rgb(255,77,255))
    t4.setFill(color_rgb(255,179,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(128,000,128))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(255,128,255))
    year2.setFill("white")
    year3 = Text(Point(360,380),"1874")
    year3.setFace("courier")
    year3.setSize(16)
    year3.setStyle("italic")
    year3.draw(win)

    win.getMouse() #year 4 (1875)
    s1.setFill(color_rgb(255,230,255))
    s2.setFill(color_rgb(255,255,255))
    t1.setFill(color_rgb(255,77,255))
    t2.setFill(color_rgb(255,77,255))
    t3.setFill(color_rgb(255,77,255))
    t4.setFill(color_rgb(255,179,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(77,000,77))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(255,77,255))
    year3.setFill("white")
    year4 = Text(Point(360,380),"1875")
    year4.setFace("courier")
    year4.setSize(16)
    year4.setStyle("italic")
    year4.draw(win)

    win.getMouse() #year 5 (1876)
    s1.setFill(color_rgb(255,230,255))
    s2.setFill(color_rgb(255,255,255))
    t1.setFill(color_rgb(230,000,230))
    t2.setFill(color_rgb(230,000,230))
    t3.setFill(color_rgb(255,77,255))
    t4.setFill(color_rgb(255,128,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(51,000,51))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(255,26,255))
    year4.setFill("white")
    year5 = Text(Point(360,380),"1876")
    year5.setFace("courier")
    year5.setSize(16)
    year5.setStyle("italic")
    year5.draw(win)

    win.getMouse() #year 6 (1877)
    s1.setFill(color_rgb(255,179,255))
    s2.setFill(color_rgb(255,26,255))
    t1.setFill(color_rgb(179,000,179))
    t2.setFill(color_rgb(230,000,230))
    t3.setFill(color_rgb(255,26,255))
    t4.setFill(color_rgb(255,77,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(51,000,51))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(179,000,179))
    year5.setFill("white")
    year6 = Text(Point(360,380),"1877")
    year6.setFace("courier")
    year6.setSize(16)
    year6.setStyle("italic")
    year6.draw(win)

    win.getMouse() #year 7 (1878)
    s1.setFill(color_rgb(255,77,255))
    s2.setFill(color_rgb(128,000,128))
    t1.setFill(color_rgb(179,000,179))
    t2.setFill(color_rgb(179,000,179))
    t3.setFill(color_rgb(230,000,230))
    t4.setFill(color_rgb(255,26,255))
    t5.setFill(color_rgb(255,230,255))
    t6.setFill(color_rgb(26,000,26))
    t7.setFill(color_rgb(102,000,102))
    t8.setFill(color_rgb(179,000,179))
    year6.setFill("white")
    year7 = Text(Point(360,380),"1878")
    year7.setFace("courier")
    year7.setSize(16)
    year7.setStyle("italic")
    year7.draw(win)
    
main()