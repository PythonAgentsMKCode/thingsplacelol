#chapter7exercise2&8
#a module to calculate the grade of a quiz given a number from 1-5
#by Treyton Opocensky

def calculateGrade():
    gradeNum = int(input("How many questions did you get correct? "))
    if gradeNum == 5:
        gradeVal = "A"
        print("You got an",gradeVal,"on that quiz.")
    elif gradeNum == 4:
        gradeVal = "B"
        print("You got a",gradeVal,"on that quiz.")
    elif gradeNum == 3:
        gradeVal = "C"
        print("You got a",gradeVal,"on that quiz.")
    elif gradeNum == 2:
        gradeVal = "D"
        print("You got a",gradeVal,"on that quiz.")
    elif gradeNum == 1:
        gradeVal = "F"
        print("You got an",gradeVal,"on that quiz.")
    elif gradeNum == 0:
        gradeVal = "F"
        print("You got an",gradeVal,"on that quiz.")
    else:
        print("The number you input does not correspond to a grade.")

def senOrRep(age,citizenAge):
    if age >= 30 and citizenAge >= 9:
        print("This person is eligible to be a US senator!")
    else:
        print("This person is not eligible to be a US senator.")
    if age >= 25 and citizenAge >= 7:
        print("This person is eligible to be a US representative!")
    else:
        print("This person is not eligible to be a US representative.")

def main():
    print("Type calculateGrade() or senOrRep(age,citizenAge)")

main()
