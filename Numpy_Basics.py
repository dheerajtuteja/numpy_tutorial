# create array 
from numpy import array 
# create array 
list1 = [1.0, 2.0, 3.0] 
a = array(list1) 

# display array 
print(a) 
# display array shape 
print(a.shape) 
# display array data type 
print(a.dtype)

# create empty array
from numpy import empty 
b = empty([3,3]) 
print(b)
#The values or content of the created array will be random and will need to be assigned before use

# create zero array 
from numpy import zeros 
c = zeros([3,5]) 
print(c)

# create one array 
from numpy import ones 
d = ones([5,2]) 
print(d)


# create array with Vertical Stack - vstack 
from numpy import array 
from numpy import vstack 
# create first array 
a1 = array([1,2,3]) 
print(a1) 
# create second array 
a2 = array([4,5,6]) 
print(a2) 
# vertical stack 
a3 = vstack((a1, a2)) 
print(a3) 
print(a3.shape)


# create array with Horizontal Stack - hstack 
from numpy import array 
from numpy import hstack 
# create first array 
b1 = array([1,2,3]) 
print(b1) 
# create second array 
b2 = array([4,5,6]) 
print(b2) 
# create horizontal stack 
b3 = hstack((b1, b2)) 
print(b3) 
print(b3.shape)


# create one-dimensional list to an array 
from numpy import array 
# list of data 
data = [11, 22, 33, 44, 55] 
# array of data 
data = array(data) 
print(data) 
print(type(data))

# create two-dimensional list to an array 
from numpy import array 
# list of data 
data1 = [[11, 22], [33, 44], [55, 66]] 
# array of data 
data1 = array(data1) 
print(data1) 
print(type(data1))


# index a one-dimensional array 
from numpy import array 
# define array 
data2 = array([11, 22, 33, 44, 55]) 
# index data 
print(data2[0]) 
print(data2[4])
#print(data2[5])
print(data2[-1])
print(data2[-5])


# index two-dimensional array 
from numpy import array 
# define array 
data3 = array([ [11, 22], [33, 44], [55, 66]]) 
# index data 
print(data3[0,0])
print(data3[0,])


# slice a one-dimensional array 
from numpy import array 
# define array 
data4 = array([11, 22, 33, 44, 55]) 
print(data4[:])
print(data4[0:1]) #starts with 0 with 1 excluded
print(data4[0:2]) #starts with 0 with 2 excluded
print(data4[1:3]) #starts with 1 with 3 excluded
print(data4[-2:]) #starts with -2 & so on -3,-4,-5 etc (in -ve order)


# slice a two-dimensional array 
from numpy import array 
# define array 
data5 = array([ [11, 22, 33], [44, 55, 66], [77, 88, 99]]) 
# separate data 
X= data5[:, :] #all rows & all columns
print(X) 
y= data5[0:1, :] #0 to 1st row (excluding 1st row) & all columns
print(y)
z=data5[:3, :] 
print(z)
w=data5[0:2, :2] 
print(w)
t=data5[2:, 1:] 
print(t)


# split train and test data 
from numpy import array 
# define array 
data = array([ [11, 22, 33], [44, 55, 66], [77, 88, 99]]) 
# separate data 
split = 2 
train,test = data[:split,:],data[split:,:] 
print(train) 
print(test)


# shape of one-dimensional array 
from numpy import array 
# define array 
data = array([11, 22, 33, 44, 55]) 
print(data.shape)


# shape of a two-dimensional array 
from numpy import array 
# list of data 
data = [[11, 22], [33, 44], [55, 66]] 
# array of data 
data = array(data) 
print(data.shape)


# row and column shape of two-dimensional array 
from numpy import array 
# list of data 
data = [[11, 22],[33, 44], [55, 66]] 
# array of data 
data = array(data) 
print('Rows: %d' % data.shape[0]) 
print('Cols: %d' % data.shape[1])


# reshape 1D array to 2D 
from numpy import array 
# define array 
data = array([11, 22, 33, 44, 55]) 
print(data)
print(data.shape) 
# reshape 
data1 = data.reshape((data.shape[0], 1)) 
print(data1.shape)
print(data1)

#reshape 2D array to 1D 
import numpy as np
a = np.array([[1, 2],
       [3, 4],
       [5, 6]])
a_flat = a.flatten()
print(a_flat)


# reshape 2D array to 3D 
from numpy import array 
# list of data 
data = [[11, 22], [33, 44], [55, 66]] 
# array of data 
data = array(data) 
print(data.shape) 
print (data)
# reshape 
data = data.reshape((data.shape[0], data.shape[1], 1)) 
print(data.shape)
print(data)

#Array Broadcasting
#Arrays with diﬀerent sizes cannot be added, subtracted, or generally be used in arithmetic. 
#A way to overcome this is to duplicate the smaller array so that it has the dimensionality 
#and size as the larger array. This is called array broadcasting

# broadcast scalar to one-dimensional array 
from numpy import array 
# define array 
a = array([1, 2, 3]) 
print(a) 
# define scalar 
b = 2 
print(b) 
# broadcast 
c = a + b #([1+2, 2+2, 3+2]) 
print(c)

# broadcast scalar to two-dimensional array 
from numpy import array 
# define array 
A = array([ [1, 2, 3], [1, 2, 3]]) 
print(A) 
# define scalar 
b = 2 
print(b) 
# broadcast 
C = A + b 
print(C)


# broadcast one-dimensional array to two-dimensional array 
from numpy import array 
# define two-dimensional array 
A = array([ [1, 2, 3], [1, 2, 3]]) 
print(A) 
# define one-dimensional array 
b = array([1, 2, 3]) 
print(b) 
# broadcast 
C = A + b 
print(C)


# broadcasting error 
from numpy import array 
# define two-dimensional array 
A = array([ [1, 2, 3], [1, 2, 3]]) 
print(A.shape) 
# define one-dimensional array 
b = array([1, 2]) 
print(b.shape) 
# attempt 
broadcast C = A + b 
print(C)

#Arithmetic, including broadcasting, can only be performed when the shape of 
#each dimension in the arrays are equal or one has the dimension size of 1.
#The dimensions are considered in reverse order, starting with the trailing dimension.