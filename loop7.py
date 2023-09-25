"""
	a program that would display all
	prime numbers(numbers that can be
	equally divided by 1 and by itself) 
	from 1 to 20
"""
import os

def main()->None:
	last:int = 20
	count:int = 0
	os.system("cls")
	#nested loop
	for i in range(1,last): #external loop
		count = 0 #nest
		for j in range(1,last):#internal loop
			if i%j == 0:
				count += 1
		if count == 2:
			print(i,end=" ")
		
if __name__=="__main__":
	main()