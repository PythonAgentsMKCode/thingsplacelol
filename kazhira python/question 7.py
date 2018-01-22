#the one question

def main():
	print("This program illustrates a chaotic function")
	X = eval(input("Enter a number between 0 and 1: "))
	Y = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		X = 2.0 * X * (1 - X)
		Y = 2.0 * Y * (1 - Y)
		print(X, Y)
