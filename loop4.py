"""
	loop exercises
	A program that would display 10 to 1
	using for
	output: 10 9 8 7 6 5 4 3 2 1
"""
from os import system

def main()->None:
	system("cls")
	for i in range(10,1,-1):
		if i%2 == 0:
			print(i,end=" ")

if __name__=="__main__":
	main()