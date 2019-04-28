# simple vector-vector arithmetic, where all operations are 
#performed element-wise between two vectors of equal length 
#to result in a new vector with the same length

# create a vector 
from numpy import array 
# define vector 
v = array([1, 2, 3]) 
print(v)

#scalar multiplication
#defince scalar
s = 0.5 
print(s) 
# multiplication 
c = s * v 
print(c)

# vector operations 
from numpy import array 
# define first vector 
a = array([5, 5, 5]) 
print(a) 
# define second vector 
b = array([1, 2, 3]) 
print(b) 
# add vectors 
c = a + b 
print(c)
# subtract vectors 
c = a - b 
print(c)
# multiplication of vectors 
c = a * b 
print(c)
# division of vectors 
c = a / b 
print(c)


# vector dot product c = (a1b1 + a2b2 + a3b3)
from numpy import array 
# define first vector 
a = array([1, 2, 3]) 
print(a) 
# define second vector 
b = array([1, 2, 3]) 
print(b) 
# multiply vectors 
c = a.dot(b) 
print(c)


#Vector Norm
#The length of the vector is referred to as the vector norm or the vector’s magnitude.
#The length of the vector is always a positive number, except for a vector of all zero values.
# Magnitude of (a,b) : ∣∣(a,b)∣∣ = [(a)^2 + (b)^2]^1/2 
# Direction of (a,b) : θ=tan^-1(b/a)
# Components from magnitude ∣∣u∣∣ and direction θ : (u cos θ, u sin θ)

#Vector L1 Norm
# ||v|| = |a1|+|a2|+|a3|
#In several machine learning applications, it is important to discriminate between 
#elements that are exactly zero and elements that are small but nonzero. 
#In these cases, we turn to a function that grows at the same rate in all locations, 
#but retains mathematical simplicity: the L1 norm.

# vector L1 norm 
from numpy import array 
from numpy.linalg import norm 
# define vector 
a = array([1, -2, -3]) 
print(a) 
# calculate L1 norm 
L1 = norm(a, 1) 
print(L1)


# ector L2 Norm
# ||v|| = [(a)^2 + (b)^2 + (c)^2]^1/2 
#The L2 norm calculates the distance of the vector coordinate from the origin of 
#the vector space. As such, it is also known as the Euclidean norm as it is calculated 
#as the Euclidean distance from the origin. 
#The result is a positive distance value. 
#The L2 norm is calculated as the square root of the sum of the squared vector values. 

# Vector L2 norm 
from numpy import array 
from numpy.linalg import norm 
# define vector 
a = array([-4, 4, -4,-4]) 
print(a) 
# calculate L2 norm 
L2 = norm(a,2) 
print(L2)

# Vector Max Norm
# The max norm is calculated as returning the maximum value of the vector
# Vec.max = max(a1,a2,a3)

# vector max norm 
import math
from numpy import inf
from numpy import array 
from numpy.linalg import norm 
# define vector 
a = array([1, 2, 3]) 
print(a) 
# calculate norm 
maxnorm = norm(a, inf) 
print(maxnorm)
