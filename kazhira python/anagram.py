#anagram.py
#a module that creates anagrams of letters in a first name
#by Treyton Opocensky

from random import randrange

dictionary = []

infile = open("dictionary.txt","r")

text = infile.readline()
while text!="":
    dictionary.append(text.replace("\n",""))
    text = infile.readline()

def isWord(word):
    """Returns true if word is stored in the online dictionary."""
    return word in dictionary
    
def main():
    name = input("Please enter your first name: ")
    name = name.lower()
    for n in range(1000):
        tempword = ""
        i1 = randrange(len(name))
        tempword += name[i1]
        i2 = randrange(len(name))
        tempword += name[i1]
        i3 = randrange(len(name))
        tempword += name[i1]
        print("One value is "+str(tempword))
    


    #resp = isWord("---")
    #print("The response for ---- was: ",resp)

main()
