#month.py
#a program to print the abbreviation of a month
#by Treyton Opocensky

def month():
    months = "JanFebMarAprMayJunJulAugSepOctNovDev"
    n = int(input("Enter a number between 1 and 12: "))
    print(months[0+3*(n-1):3+3*(n-1)])

def grade():
    grades = "FFDCBA"
    n = int(input("Enter the number of correct questions: "))
    print("The grade you recieved for", n, "points is:", grades[n])

def wordcount():
    string = str(input("Enter a sentence: "))
    wordcount = string.count(" ") + 1
    print("There are", wordcount, "words in that sentence.")
  
def acronym():
    acronym = ""
    phrase = input("Enter a phrase: ")
    phrase = phrase.upper()
    tokens = phrase.split(" ")
    for word in tokens:
        acronym += word[0]
    print("The acronym is:", acronym)

def count():
    sentence = input("Enter a sentence: ")
    sentence.count('a','b','c')
    print(sentence.count)
    
def main():
    print("Type month() or grade() or wordcount()or acronym() to use this files functions.")

def AverageWordLength():
    sumwordlength = 0
    thePhrase = input("Please enter a sentence: ")
    tokens = thePhrase.split(" ")
    for word in tokens:
        tempword = word
        tempword = tempword.rstrip()
        tempword = tempword.replace(".","")
        sumwordlength += len(tempword)

    avg = sumwordlength/len(tokens)
    print("The average word length is " + str(avg) + ".")

def Anagram

main()











