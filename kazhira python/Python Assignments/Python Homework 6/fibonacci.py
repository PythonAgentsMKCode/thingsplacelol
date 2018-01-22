#fibonacci.py

def fib(n):
    fibList = [0,1]
    while n > len(fibList)-1:
        fibList.append(fibList[len(fibList)-1] + fibList[len(fibList)-2])
    return fibList[n]
