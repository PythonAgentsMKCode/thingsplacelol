#MSDie.py
#by Zelle
#a class definition for a multi-sided die

from random import randrange

class MSDie:

    def __init__(self,sides):
        self.sides = sides
        self.value = 1
        #sets some default value for every attribute

    def roll(self):
        self.value = randrange(1,self.sides+1)
        #puts a random value into self.value

    def getValue(self):
        return self.value
        #returns value created at __init__ or roll

    def setValue(self,newValue):
        self.value = newValue
        #puts a set new value into self.value
        
    def getSides(self):
        return self.sides
