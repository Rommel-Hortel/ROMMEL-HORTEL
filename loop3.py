"""
	loop exercises
	A program that would display 10 to 1
	using while
	output: 10 9 8 7 6 5 4 3 2 1
"""
from os import system

def main()->None:
	system("cls")
	i:int = 10
	while i>0:
		print(i,end=" ")
		i -= 1

if __name__ == "__main__":
	main()
