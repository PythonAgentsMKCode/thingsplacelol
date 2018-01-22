#squareEach.py

def squareEach(nums):
    for i in nums:
        nums = [i*i]
    print(nums)
    
squareEach([1,2,3,4,5])
