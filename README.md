# Simple-Matrix-Calculator
# Simple Matrix Calculator

## Overview
The **Simple Matrix Calculator** is a Python-based program that allows users to perform basic matrix operations such as addition, subtraction, multiplication, and transposition using the NumPy library. The program provides an interactive menu-driven interface for easy matrix computations.

## Features
- Addition of two matrices
- Subtraction of two matrices
- Multiplication of two matrices (dot product)
- Transposing a matrix
- User-friendly input system

## Requirements
Ensure you have Python installed along with the NumPy library. If NumPy is not installed, you can install it using:
```bash
pip install numpy
```

## How to Use
1. Run the Python script.
2. Enter the dimensions (rows and columns) of the matrices.
3. Input the values for two matrices.
4. Select an operation from the menu:
   - 1: Addition
   - 2: Subtraction
   - 3: Multiplication
   - 4: Transpose
   - 5: Exit
5. View the results and continue calculations as needed.

## Example Usage
```plaintext
Enter the matrix 1,
Note:-both matrix 1 and 2 must have same dimension
Enter the number of rows: 2
Enter the number of cols: 2
Enter values of row 1 & col 1: 1
Enter values of row 1 & col 2: 2
Enter values of row 2 & col 1: 3
Enter values of row 2 & col 2: 4

Enter the matrix 2,
Note:-both matrix 1 and 2 must have same dimension
Enter values of row 1 & col 1: 5
Enter values of row 1 & col 2: 6
Enter values of row 2 & col 1: 7
Enter values of row 2 & col 2: 8
```

**Operations Output:**
```plaintext
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Exit

Enter your choice: 1
Matrix 1:
[[1 2]
 [3 4]]
Matrix 2:
[[5 6]
 [7 8]]
The addition of matrices is:
[[ 6  8]
 [10 12]]
```

## Notes
- Ensure that both matrices have the same dimensions for addition and subtraction.
- For multiplication, the number of columns in the first matrix must match the number of rows in the second matrix.
- The program uses `numpy.dot()` for correct matrix multiplication.

## License
This project is open-source and free to use.

