#                                           Project Title: Simple Matrix Calculator

# Import the NumPy library.
import numpy as np
import os
# Defining  functions for matrix operations

# Addition of two matrices.
def matrix_addition(mat1,mat2):
    return mat1+mat2

# Subtraction of two matrices.
def matrix_substraction(mat1,mat2):
    return mat1-mat2

# Multiplication of two matrices.
def matrix_multiplication(mat1,mat2):
    return np.dot(mat1,mat2)

# Transposing a matrix.
def transpose_matrix(mat):
    return mat.T

def get_matrix():
    out_list=[]
    rows=int(input('Enter the no. of rows:'))
    cols=int(input('Enter the no. of cols:'))
    matrix=[]
    for i in range(rows):
        out_list=[]
        for j in range(cols):
            k=int(input(f'Enter values of row {i+1}& col {j+1} :'))
            out_list.append(k)
        matrix.append(out_list)
    return np.array([matrix])



# Accept user input for two matrices.

print('Enter the matrix 1,'
      '\nNote:-both matrix 1 and 2 must have same dimension')
matrix1=get_matrix()
print(matrix1)
print('\n\nEnter the matrix 2,'
      '\nNote:-both matrix 1 and 2 must have same dimension')
matrix2=get_matrix()
print(matrix2)

# Display a menu with options for different operations.
while True:
    os.system('cls')
    print('                             Simple Matrix Calculator                                    ')
    print('1.Addition'
        '\n2.Substraction'
        '\n3.Multiplication'
        '\n4.Transpose'
        '\n5.Exit\n\n')

    try:
        user_choice=int(input('Enter your choice : '))
    except ValueError:
        print('Please enter integer only')
    if user_choice==1:
        add=matrix_addition(matrix1,matrix2)
        print(f'Matrix 1 : {matrix1}\nMatrix 2 : {matrix2}\nThe addition of matrixes are {add}')
    elif user_choice==2:
        add=matrix_substraction(matrix1,matrix2)
        print(f'Matrix 1 : {matrix1}\nMatrix 2 : {matrix2}\nThe substraction of matrixes are {add}')
    elif user_choice==3:
        add=matrix_multiplication(matrix1,matrix2)
        print(f'Matrix 1 : {matrix1}\nMatrix 2 : {matrix2}\nThe multiplication of matrixes are {add}')
    elif user_choice==4:
        add1=transpose_matrix(matrix1)
        add2=transpose_matrix(matrix2)
        print(f'Matrix 1 : {matrix1}\nMatrix 2 : {matrix2}\nThe Transpose of matrixe 1 is {add1}\nThe Transpose of matrixe 2 is {add2}')
    elif user_choice==5:
        break
    input('\nPress Enter to continue')