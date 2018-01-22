#rwbyVote.py
#a module to vote for the best member of Team RWBY
#by Treyton Opocensky

from graphics import *

def backGround(win):
    #this makes the background gray
    backGround = Rectangle(Point(0,0),Point(720,480))
    backGround.setFill("gray")
    backGround.draw(win)

def rwbySquares(win):
    #this draws team RWBY's colored squares
    rubySquare = Rectangle(Point(67,395),Point(77,405))
    rubySquare.setFill("red")
    rubySquare.setOutline("red")
    rubySquare.draw(win)
    
    weissSquare = Rectangle(Point(139,395),Point(149,405))
    weissSquare.setFill("white")
    weissSquare.setOutline("white")
    weissSquare.draw(win)
    
    blakeSquare = Rectangle(Point(211,395),Point(221,405))
    blakeSquare.setFill("black")
    blakeSquare.setOutline("black")
    blakeSquare.draw(win)
                        
    yangSquare = Rectangle(Point(283,395),Point(293,405))
    yangSquare.setFill("yellow")
    yangSquare.setOutline("yellow")
    yangSquare.draw(win)

    
def jnprSquares(win):
    #this colors team JNPR's colored squares
    jauneSquare = Rectangle(Point(427,395),Point(437,405))
    jauneSquare.setFill("yellow")
    jauneSquare.setOutline("yellow")
    jauneSquare.draw(win)
    
    noraSquare = Rectangle(Point(499,395),Point(509,405))
    noraSquare.setFill("pink")
    noraSquare.setOutline("pink")
    noraSquare.draw(win)
    
    pyrrhaSquare = Rectangle(Point(571,395),Point(581,405))
    pyrrhaSquare.setFill("red")
    pyrrhaSquare.setOutline("red")
    pyrrhaSquare.draw(win)
    
    renSquare = Rectangle(Point(643,395),Point(653,405))
    renSquare.setFill("green")
    renSquare.setOutline("green")
    renSquare.draw(win)

def bestChars(win):
    #this draws the big circle on the left
    bestRWBY = Circle(Point(180,175),150)
    bestRWBY.setFill("blue")
    bestRWBY.draw(win)

    #this draws the buttons at the bottom for team RWBY, and the text inside them
    rubyClick = Rectangle(Point(0,440),Point(89,480))
    rubyClick.setFill("white")
    rubyClick.setOutline("black")
    rubyClick.draw(win)
    rubyWord = Text(Point(45,460),"Ruby")
    rubyWord.setFace("courier")
    rubyWord.setSize(16)
    rubyWord.draw(win)
    
    weissClick = Rectangle(Point(90,440),Point(179,480))
    weissClick.setFill("white")
    weissClick.setOutline("black")
    weissClick.draw(win)
    weissWord = Text(Point(135,460),"Weiss")
    weissWord.setFace("courier")
    weissWord.setSize(16)
    weissWord.draw(win)
    
    blakeClick = Rectangle(Point(180,440),Point(269,480))
    blakeClick.setFill("white")
    blakeClick.setOutline("black")
    blakeClick.draw(win)
    blakeWord = Text(Point(225,460),"Blake")
    blakeWord.setFace("courier")
    blakeWord.setSize(16)
    blakeWord.draw(win)
    
    yangClick = Rectangle(Point(270,440),Point(359,480))
    yangClick.setFill("white")
    yangClick.setOutline("black")
    yangClick.draw(win)
    yangWord = Text(Point(315,460),"Yang")
    yangWord.setFace("courier")
    yangWord.setSize(16)
    yangWord.draw(win)

    #this draws the big circle on the right
    bestJNPR = Circle(Point(540,175),150)
    bestJNPR.setFill("blue")
    bestJNPR.draw(win)

    #this sets the count of each character to start at 0
    rubyCount = 0
    weissCount = 0
    blakeCount = 0
    yangCount = 0
    jauneCount = 0
    noraCount = 0
    pyrrhaCount = 0
    renCount = 0

    #this draws the buttons at the bottom for team JNPR, and the text inside them
    jauneClick = Rectangle(Point(360,440),Point(449,480))
    jauneClick.setFill("white")
    jauneClick.setOutline("black")
    jauneClick.draw(win)
    jauneWord = Text(Point(405,460),"Jaune")
    jauneWord.setFace("courier")
    jauneWord.setSize(16)
    jauneWord.draw(win)

    noraClick = Rectangle(Point(450,440),Point(539,480))
    noraClick.setFill("white")
    noraClick.setOutline("black")
    noraClick.draw(win)
    noraWord = Text(Point(495,460),"Nora")
    noraWord.setFace("courier")
    noraWord.setSize(16)
    noraWord.draw(win)

    pyrrhaClick = Rectangle(Point(540,440),Point(629,480))
    pyrrhaClick.setFill("white")
    pyrrhaClick.setOutline("black")
    pyrrhaClick.draw(win)
    pyrrhaWord = Text(Point(585,460),"Pyrrha")
    pyrrhaWord.setFace("courier")
    pyrrhaWord.setSize(16)
    pyrrhaWord.draw(win)

    renClick = Rectangle(Point(630,440),Point(720,480))
    renClick.setFill("white")
    renClick.setOutline("black")
    renClick.draw(win)
    renWord = Text(Point(675,460),"Ren")
    renWord.setFace("courier")
    renWord.setSize(16)
    renWord.draw(win)

    #this draws the counters in for each character
    rubyCounter = Text(Point(72,370),rubyCount)
    rubyCounter.setFace("courier")
    rubyCounter.setSize(16)
    rubyCounter.draw(win)
    
    weissCounter = Text(Point(144,370),weissCount)
    weissCounter.setFace("courier")
    weissCounter.setSize(16)
    weissCounter.draw(win)
    
    blakeCounter = Text(Point(216,370),blakeCount)
    blakeCounter.setFace("courier")
    blakeCounter.setSize(16)
    blakeCounter.draw(win)
    
    yangCounter = Text(Point(288,370),yangCount)
    yangCounter.setFace("courier")
    yangCounter.setSize(16)
    yangCounter.draw(win)
    
    jauneCounter = Text(Point(432,370),jauneCount)
    jauneCounter.setFace("courier")
    jauneCounter.setSize(16)
    jauneCounter.draw(win)
    
    noraCounter = Text(Point(504,370),noraCount)
    noraCounter.setFace("courier")
    noraCounter.setSize(16)
    noraCounter.draw(win)
    
    pyrrhaCounter = Text(Point(576,370),pyrrhaCount)
    pyrrhaCounter.setFace("courier")
    pyrrhaCounter.setSize(16)
    pyrrhaCounter.draw(win)
    
    renCounter = Text(Point(648,370),renCount)
    renCounter.setFace("courier")
    renCounter.setSize(16)
    renCounter.draw(win)

    #this sets the code to funtion foir an undending number of clicks

    close = Rectangle(Point(700,0),Point(720,20))
    close.setFill("white")
    close.setOutline("black")
    close.draw(win)
    closeText = Text(Point(710,10),"X")
    closeText.setFace("courier")
    closeText.setSize(16)
    closeText.draw(win)
    

    while True:

        mouse = win.getMouse()
        
        #this changes the color of the circles and ticks up the counter each click
        if rubyClick.p1.x < mouse.x < rubyClick.p2.x and rubyClick.p1.y < mouse.y < rubyClick.p2.y:
            bestRWBY.setFill("red")
            rubyCounter.undraw()
            rubyCount = rubyCount + 1
            rubyCounter = Text(Point(72,370),rubyCount)
            rubyCounter.setFace("courier")
            rubyCounter.setSize(16)
            rubyCounter.draw(win)
            
        elif weissClick.p1.x < mouse.x < weissClick.p2.x and weissClick.p1.y < mouse.y < weissClick.p2.y:
            bestRWBY.setFill("white")
            weissCounter.undraw()
            weissCount = weissCount + 1
            weissCounter = Text(Point(144,370),weissCount)
            weissCounter.setFace("courier")
            weissCounter.setSize(16)
            weissCounter.draw(win)

        elif blakeClick.p1.x < mouse.x < blakeClick.p2.x and blakeClick.p1.y < mouse.y < blakeClick.p2.y:
            bestRWBY.setFill("black")
            blakeCounter.undraw()
            blakeCount = blakeCount + 1
            blakeCounter = Text(Point(216,370),blakeCount)
            blakeCounter.setFace("courier")
            blakeCounter.setSize(16)
            blakeCounter.draw(win)

        elif yangClick.p1.x < mouse.x < yangClick.p2.x and yangClick.p1.y < mouse.y < yangClick.p2.y:
            bestRWBY.setFill("yellow")
            yangCounter.undraw()
            yangCount = yangCount + 1
            yangCounter = Text(Point(288,370),yangCount)
            yangCounter.setFace("courier")
            yangCounter.setSize(16)
            yangCounter.draw(win)

        elif jauneClick.p1.x < mouse.x < jauneClick.p2.x and jauneClick.p1.y < mouse.y < jauneClick.p2.y:
            bestJNPR.setFill("yellow")
            jauneCounter.undraw()
            jauneCount = jauneCount + 1
            jauneCounter = Text(Point(432,370),jauneCount)
            jauneCounter.setFace("courier")
            jauneCounter.setSize(16)
            jauneCounter.draw(win)

        elif noraClick.p1.x < mouse.x < noraClick.p2.x and noraClick.p1.y < mouse.y < noraClick.p2.y:
            bestJNPR.setFill("pink")
            noraCounter.undraw()
            noraCount = noraCount + 1
            noraCounter = Text(Point(504,370),noraCount)
            noraCounter.setFace("courier")
            noraCounter.setSize(16)
            noraCounter.draw(win)

        elif pyrrhaClick.p1.x < mouse.x < pyrrhaClick.p2.x and pyrrhaClick.p1.y < mouse.y < pyrrhaClick.p2.y:
            bestJNPR.setFill("red")
            pyrrhaCounter.undraw()
            pyrrhaCount = pyrrhaCount + 1
            pyrrhaCounter = Text(Point(576,370),pyrrhaCount)
            pyrrhaCounter.setFace("courier")
            pyrrhaCounter.setSize(16)
            pyrrhaCounter.draw(win)

        elif renClick.p1.x < mouse.x < renClick.p2.x and renClick.p1.y < mouse.y < renClick.p2.y:
            bestJNPR.setFill("green")
            renCounter.undraw()
            renCount = renCount + 1
            renCounter = Text(Point(648,370),renCount)
            renCounter.setFace("courier")
            renCounter.setSize(16)
            renCounter.draw(win)
            
        elif close.p1.x < mouse.x < close.p2.x and close.p1.y < mouse.y < close.p2.y:
            win.close()
            return

def main():
    win = GraphWin("Vote for the best RWBY character",720,480)
    backGround(win)
    rwbySquares(win)
    jnprSquares(win)
    bestChars(win)

main()
