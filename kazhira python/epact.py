#epact

def main():
    print("This program displays the epact for a given year.")
    print()
    year = int(input("What year do you wish to find the epact for? "))
    c = year // 100
    epact = (8+(c//4)-c+((8*c+13)//25)+11*(year%19))%30
    print()
    print("The epact for that year is", epact, ".")

main()
