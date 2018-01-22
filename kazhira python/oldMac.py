#oldMac.py
#a program to print the lyrics of the song "Old MacDonald"
#by Treyton Opocensky

def hadAFarm():
    print("Old MacDonald had a farm, Ee-igh, Ee igh, Oh!")

def oldMac(animal,sound):
    hadAFarm()
    print("And on that farm he had a",animal+", Ee-igh, Ee igh, Oh!")
    print("With a",sound+",",sound,"here and a",sound+",",sound,"there.")
    print("Here a",sound+", there a",sound+", everywhere a",sound+",",sound +".")
    hadAFarm()
    print()

def main():
    oldMac("cow","moo")
    oldMac("pig","oink")
    oldMac("chicken","cluck")
    oldMac("sheep","baa")
    oldMac("horse","neigh")

main()
