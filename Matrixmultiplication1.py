"""
   ROMARES, TIMOTHY NOEL
   BSIT 3C 1:30PM-3:00PM)
   
"""

from os import system 
def main()-> None:
 system("cls")
 
 def matrix_multiply(matrix_a,matrix_b):
 rows_a= len(matrix_a)
 cols_a=len(matrix_a[0])
 rows_b=len(matrix_b)
 cols_b =len(matrix_b[0])
 
 if cols_a != rows_b:
   print("Matrix multiplication is not possible")
 
 result=[[0 for_in range (cols_b)] for_in range(rows_a)]
   
  for i in range(rows_a):
    for j in range(cols_b):
	   for k in range(cols_a):
	      result[i][j] += matrix_a[i][k] *
		    matrix_b[k][i]
			print(result)
			
 
 matrix_a:list =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
 
 ]
 mstrix_b = [
  [5,4,3],
  [1,2,6],
  [7,9,8]
 ]
 
 for row in result_matrix:
    print(row)