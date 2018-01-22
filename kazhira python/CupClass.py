#cupClass.py
#a class definition for a cup

class Cup:

    def __init__(self,beverageType):
        self.beverageType = beverageType
        self.howFull = "100%"
        
    def drink(self):
        if self.howFull == "100%":
            self.howFull = "75%"
        elif self.howFull == "75%":
            self.howFull = "50%"
        elif self.howFull == "50%":
            self.howFull = "25%"
        elif self.howFull == "25%":
            self.howFull = "Empty"
        else:
            print("Your drink is empty.")
                  
    def dumpOut(self):
        self.howFull = "Empty"
                  
    def refill(self):
        self.howFull = "100%"
