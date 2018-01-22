#craps.py
#a module to play games of craps and report statistics
#by Treyton Opocensky

from random import random

def multipleGames(num):
    wins = 0
    losses = 0
    for i in range(num):
        win, loss, = oneGame()
        wins = wins + win
        losses = losses + loss
    return wins, losses
    
def oneGame():
    win = 0
    loss = 0
    newRoll = 0
    firstDie = int(random()*6)+1
    secondDie = int(random()*6)+1
    firstRoll = firstDie + secondDie

    if firstRoll == 7 or firstRoll== 11:
        win = 1
    elif firstRoll == 2 or firstRoll == 3 or firstRoll == 12:
        loss = 1
    else:
        win, loss = rollPoints(firstRoll)
    return win, loss

def rollPoints(initial):
    win = 0
    loss = 0
    newRoll = 0
    while newRoll != initial:
        newRoll = (int(random()*6) + 1) + (int(random()*6) + 1)
        if newRoll == 7:
            loss = 1
            return win, loss
    win = 1
    return win, loss
    
def main():
    numGames = eval(input("How many games would you like to play? "))
    wins, losses, = multipleGames(numGames)
    print()
    print("Games =", numGames)
    print("Wins =", wins)
    print("Losses =", losses)
    print()
    print("The % chance of winning is", (wins / numGames)*100, "%")
    print("(About", int((wins / numGames) * 100), "%)")

main()

'''if the roll is 2, 3, 12, player loses
   if the roll is 7, 11,    player wins
   anything else            keep rolling
   rerolls before 7         player wins
   rerolls 7                player loses'''
