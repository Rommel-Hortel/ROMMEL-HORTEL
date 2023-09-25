"""
	loop exercises
	A program that would display all odd numbers
	1 to 10
	output: 1 3 5 7 9
"""
import os

def main()->None:
	os.system("cls")
	for i in range(1,11):
		if i%2>0:
			print(i,end=" ")

if __name__=="__main__":
	main()