#CupTest.py
#a file to test the Cup class

from CupClass import Cup

cupWater = Cup("water")
cupSoda = Cup("soda")
cupMilk = Cup("milk")

cupWater.drink()
cupSoda.dumpOut()
cupMilk.drink()
cupMilk.refill()

print("Water", cupWater.howFull,
      "Soda", cupSoda.howFull,
      "Milk", cupMilk.howFull)
