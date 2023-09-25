"""
	Name :<>
	Lab Schedule:<12:30 - 3:30>
	
	Create a program that would accept a positive integer
	not greater than 15, the value correspond to the last
	value to be printed in the format shown below
	example:
		input : 10
		output :
		1 2 3 4 5 6 7 8 9 10
		2 3 4 5 6 7 8 9
		3 4 5 6 7 8
		4 5 6 7
		5 6
		6
		
		input: 5
		1 2 3 4 5
		2 3 4
		3
		
		input: 7
		1 2 3 4 5 6 7
		2 3 4 5 6
		3 4 5
		4 
		
		
		
		
"""
from os import system

def main()->None:
    system("cls")
a = int(input("Input: "))
if a > 1 <= 15:
	for i in range(1,a+1):
		for j in range (i,a,1):
			print(j, end =" ")
		print()

if __name__=="__main__":
	main()



