#rball.py
#by Zelle, adapted by Treyton Opocensky
#a program to simulate a racquetball game
from random import random

def main():
    printIntro()
    probA, probB, n, m = getInputs()
    matchesA, matchesB = simNMatches(n, m, probA, probB)
    printSummary(matchesA, matchesB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by the probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve")
    print()

def getInputs():
    # Returns the three papameters
    a = float(input("What is the prob. Player A wins a serve? "))
    b = float(input("What is the prob. Player B wins a serve? "))
    n = int(input("How many games in a match? "))
    m = int(input("How many matches? "))
    return a, b, n, m

def simNMatches(n, m, probA, probB):
    matchesA = 0
    matchesB = 0
    for i in range(m):
        winsA, winsB = simNGames(n, probA, probB)
        if winsA > winsB:
            matchesA = matchesA + 1
        else:
            matchesB = matchesB + 1
    return matchesA, matchesB


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, n):
    # Simulates a single game of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns final scores for A and B
    i=0
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB, n):
        if i%2 == 0:
            serving = "A"
        elif i%2 == 1:
            serving = "B"
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
        elif serving == "B":
            if random() < probB:
                scoreB = scoreB + 1
        i = i + 1
        return scoreA, scoreB

def gameOver(a, b, n):
    # a and b represent scores for a racquetball game
    # Returns true if the game is over, False otherwise
    return a >= .5 * n or b >= .5 * n

def printSummary(matchesA, matchesB):
    # Prints a sumamry of wins for each player
    m = matchesA + matchesB
    print("\nMatches simulated", m)
    print("Matches for A: {0} ({1:0.1%})".format(matchesA, matchesA/m))
    print("Matches for B: {0} ({1:0.1%})".format(matchesB, matchesB/m))

if __name__ == '__main__': main()
