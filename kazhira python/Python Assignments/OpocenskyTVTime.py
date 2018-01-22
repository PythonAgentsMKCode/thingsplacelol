#OpocenskyService.py
#Treyton Opocensky
#A program to calculate the total amount of time required to watch a television show!

def main():
    print("This program can calculate the amount of time required (in minutes)")
    print("to watch a television show!")
    print()
    episodeNum = eval(input("How many episodes do you want to watch? (ex. 10) "))
    episodeTime = eval(input("How long are these episodes? (ex. 24.10 for 24 mins 10 secs) "))
    print()
    print("The amount of time required to watch this show is", episodeNum * episodeTime, "minutes!")
    hours = int(((episodeNum * episodeTime) / 60) * 100) / 100
    print("Or", hours, "hours!")
main()
