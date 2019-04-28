# A matrix is a two-dimensional array (a table) of numbers.

# create matrix 
from numpy import array 
A = array([[1, 2, 3], [4, 5, 6]]) 
print(A) # 2 Rows & 3 Columns


# Matrix Operations

# Two matrices must have same dimensions

 
from numpy import array 
# define first matrix 
A = array([ [1, 2, 3], [4, 5, 6]]) 
print(A) 
# define second matrix 
B = array([ [1, 2, 3], [4, 5, 6]]) 
print(B) 
# matrix addition 
C = A + B 
print(C)
# matrix subtraction 
C = A - B 
print(C)
# matrix multiplication 
C = A * B 
print(C)
# matrix division 
C = A / B 
print(C)
# matrix scalar multiplication 
C = A * 5
print(C)


# Matrix-Matrix Multiplication

# A = 2 X 3
# B = 3 X 5
# C = A.dotB= 2 X 5 (Result)

# Count of Columns in 1st Matrix = Count of Row in the second matrix

# matrix dot product 
from numpy import array 
# define first matrix 
A = array([ [1, 2], [3, 4], [5, 6]]) 
print(A) 
# define second matrix 
B = array([ [1, 2], [3, 4]]) 
print(B) 
# multiply matrices 
C = A.dot(B) 
print(C) 

# Matrix-Vector Multiplication

# A matrix and a vector can be multiplied together as long as the rule 
# of matrix multiplication is observed.

# matrix-vector multiplication 
from numpy import array 
# define matrix 
A = array([ [1, 2], [3, 4], [5, 6]]) 
print(A) 
# define vector 
B = array([0.5, 0.5]) 
print(B) 
# multiply 
C = A.dot(B) 
print(C)


# Types of Matrices

# Square Matrix

# A square matrix is a matrix where the number of rows (n) is equivalent 
# to the number of columns (m).
# n ≡ m

# Symmetric Matrix

# A symmetric matrix is a type of square matrix where the top-right triangle 
# is the same as the bottom-left triangle.
# A symmetric matrix is always square and equal to its own transpose.
# M = M^T

# Triangular Matrix

# A triangular matrix is a type of square matrix that has all values in the upper-right 
# or lower-left of the matrix with the remaining elements ﬁlled with zero values. 
# A triangular matrix with values only above the main diagonal is called an upper triangular matrix. 
# Whereas, a triangular matrix with values only below the main diagonal is called a lower triangular matrix.

# triangular matrices 
from numpy import array 
from numpy import tril 
from numpy import triu 
# define square matrix 
M = array([ [1, 2, 3], [1, 2, 3], [1, 2, 3]]) 
print(M) 
# lower triangular matrix 
lower = tril(M) 
print(lower) 
# upper triangular matrix 
upper = triu(M) 
print(upper)

# Diagonal Matrix
# A diagonal matrix is one where values outside of (other than) 
#the main diagonal have a zero value

from numpy import array 
from numpy import diag 
# define square matrix 
M = array([ [1, 2, 3], [1, 2, 3], [1, 2, 3]]) 
print(M) 
# extract diagonal vector 
d = diag(M) 
print(d) 
# create diagonal matrix from vector 
D = diag(d) 
print(D)

# Identity Matrix
# An identity matrix is a matrix that does not change any vector 
# when we multiply that vector by that matrix.

from numpy import identity 
I = identity(3) 
print(I)

# Orthogonal Matrix

# Two vectors are orthogonal when their dot product equals zero.
# The length of each vector is 1 then the vectors are called orthonormal 
# because they are both orthogonal and normalized.

# Properties of Orthogonal Matrix
# Qtranspose ·Q = Q·Qtranspose = I (Indentity)
# Qtranspose = QInverse
# Orthogonal matrices are used a lot for linear transformations, 
# such as reﬂections and permutations.


from numpy import array 
from numpy.linalg import inv 
# define orthogonal matrix 
Q = array([ [1, 0], [0, -1]]) 
print(Q) 
# inverse equivalence 
V = inv(Q) 
print(V) 
# identity equivalence 
I = Q.dot(V) 
print(I)


# Key Matrix Operations

# Transpose
# A deﬁned matrix can be transposed, which creates a new matrix with 
# the number of columns and rows ﬂipped.

# transpose matrix 
from numpy import array 
# define matrix 
A = array([ [1, 2], [3, 4], [5, 6]]) 
print(A) 
# calculate transpose 
C = A.T 
print(C)


# Inverse

# Matrix inversion is a process that ﬁnds another matrix that when multiplied with the matrix, 
# results in an identity matrix

# invert matrix 
from numpy import array 
from numpy.linalg import inv 
# define matrix 
A = array([ [1.0, 2.0], [3.0, 4.0]]) 
print(A) 
# invert matrix 
B = inv(A) 
print(B) 
# Check - multiply A and B 
I =  A.dot(B) 
print(I)

# Trace
#A trace of a square matrix is the sum of the values on the main diagonal of the matrix

# matrix trace 
from numpy import array 
from numpy import trace 
# define matrix 
A = array([ [1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(A) 
# calculate trace 
B = trace(A) 
print(B)

# Determinant
# The determinant of a square matrix is a scalar representation of the volume of the matrix.

from numpy import array 
from numpy.linalg import det 
# define matrix 
A = array([ [1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(A) 
# calculate determinant 
B = det(A) 
print(B)

# Relation between Inverse & Determination
# A^-1 = adjoint(A) / determinant(A)
# adjoint(A) = Transpose of the Cofactors of A

import numpy as np
# define matrix 
A = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(A) 
#Hermitian adjoint
B1 = (A.T.conj())
print(B1)
# calculate determinant 
B2 = det(A) 
print(B2)
#Inverse
print(B1/B2)
#Check Inverse
B = inv(A)
print(B)

#Rank of a matrix

#The rank of a matrix is the estimate of the number of linearly independent 
#rows or columns in a matrix. The rank of a matrix M is often denoted as 
#the function rank().

from numpy import array 
from numpy.linalg import matrix_rank 
# rank 
v1 = array([1,2,3]) 
print(v1) 
vr1 = matrix_rank(v1) 
print(vr1) 
# zero rank 
v2 = array([0,0,0,0,0]) 
print(v2) 
vr2 = matrix_rank(v2) 
print(vr2)
