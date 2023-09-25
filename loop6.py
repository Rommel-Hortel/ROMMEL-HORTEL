"""
	loop exercises
	A program that would display 1 to 10
	using a list and list comprehension
	output: 1 2 3 4 5 6 7 8 9 10
"""
import os

def main()->None:
	values:list = [1,2,3,4,5,6,7,8,9,10]
	os.system("cls")
	#for v in values: print(v,end=" ")
	#list comprehension
	[print(v,end=" ") for v in values if v%2==0]
	
if __name__=="__main__":
	main()