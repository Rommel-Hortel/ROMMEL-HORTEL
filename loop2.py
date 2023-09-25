"""
	
loop exercises
	A program that would display 1 to 10
	using for
	output: 1 2 3 4 5 6 7 8 9 10
"""
from os import system

def main()->None:
	system("cls")
	for i in range(1,11):
		print(i,end = " ")

if __name__ == "__main__":
	main()