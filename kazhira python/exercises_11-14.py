#exercises_11-14.py
#a program to square a list of numbers
#by Treyton Opocensky

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return
    
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return

def sumList(nums):
    theSum = 0
    for i in range(len(nums)):
        theSum = theSum + nums[i]
    return theSum

def main():
    infile = open("numbers.txt","r")
    strList = infile.readlines()
    toNumbers(strList)
    nums = strList
    squareEach(nums)
    mySum = sumList(nums)
    print("The sum is",mySum,".")

    outfile = open("numOut.txt","w")
    print("Here are the square numbers and sum:",file=outfile)
    for num in nums:
        print(num,file=outfile)
    print("The sum is",mySum,file=outfile)

    outfile.close()

main()
