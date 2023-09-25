"""
	A program that would accept a positive integer value
	not greater 15, display the numerical format as shown below
	enter value(n): 5
	1 2 3 4 5
	2 3 4 
	3
"""
from os import system
def main()->None:
	start:int = 1
	system("cls")
	n:int = int(input("Enter value(n):"))
	#validation
	if n>0 and n<16:
		for i in range((n+1),start,-1):
			for j in range(start,i):
				print(j,end=" ")
			print("")
			start += 1
	
if __name__=="__main__":
	main()


