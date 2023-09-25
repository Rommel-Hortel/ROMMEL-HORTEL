"""
	loop exercises
	A program that would display 1 to 10
	using while
	output: 1 2 3 4 5 6 7 8 9 10
"""
from os import system
def main()->None:
	system("cls")
	#initialization
	i:int = 1
	#loop condition
	while i<11:
	#repeated operation
		print(i,end=" ")
		#iteration
		i += 1 # i=i+1
	
#trigger
if __name__ == "__main__":
	main()
