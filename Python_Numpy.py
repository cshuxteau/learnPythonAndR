import numpy as np

# An ndarray is a generic multidimensional container for homogeneous data;
# that is, all of the elements must be the same type.
# It is similar in function to R Matrix

# create numpy.ndarray by using np.arrange
x = np.arange(1000000)
print(type(x))
for _ in range(10): y = x * 2
print(y[0:10:2])

x = np.random.randn(2, 3) # create a 2x3 array
# An ndarray is a generic multidimensional container for homogeneous data;
print(x.shape)
print(x.dtype)

#====================================
# create a ndarray
#====================================
import numpy as np

x  = [1, 2, 3,4, 5, 6];
y = np.array(x);
print(y.shape)

x  = (1, 2, 3,4, 5, 6 );
y = np.array(x);
print(y.shape)

x = [[1, 2, 3, 4], [5, 6, 7, 8]]
y = np.array(x);
print(y.shape)

# multi-dimentional array
x = np.array([1, 2, 3], dtype=np.int32)

x = np.zeros((3, 6))
print(x);

y = x.astype(np.int64)
print(y.dtype)

#====================================
# ndarray arithmetic
#====================================
# vectorization: operation applies at element level
x = np.array([[1., 2., 3.], [4., 5., 6.]])
print(1/x)

#====================================
# access ndarray elements
#====================================
x = np.arange(10)
print(x[5:8]) # similar to R vector and List access

# change slice will update the original array
x = np.arange(10)
print(x) # similar to R vector and List access

# change slice will update the original array
# a.k.a: slice produces a view, not actual copy
s = x[0:2]
s[0] = 11
print(x)
c = x[0:2].copy()
c[0] = 12
print(x)

# two dimension
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x[0][2])
print(x[0,2])   #similar to R matrix
print(x[:2]) # print first 2 rows (2 is the upper bound for the axis that is excluded)
print(x[:2,1:]) # similar to R matrix
print( x[:, :1]) #slightly different than R; R does not need : if you need the entire axis

# boolean indexing
x = np.random.randn(7, 3)
letters = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(x[letters == 'b'])  # select the 2nd row from x
print(x[letters != 'b'])  # select the 2nd row from x
filter = (letters == 'b') | (letters == 'c')
print(x[ ~ filter ])  # select the 2nd row from x
print(x[letters == 'b', :2])  # select the 2nd row from x
print(x[x < 0]) # similar to WHICH in R; return a one dimension array

# use fancy index to get a two dimension array
x = np.arange(32).reshape((8, 4))
# fancy indexing, unlike slicing, always copies the data into a new array.
print(x[[1, 5, 7, 2], [0, 3, 1, 2]])  #print one dimension array
print(x[[1, 5, 7, 2]][:, [0, 3, 1, 2]])  #print two dimnsion array
print(x.T)   #similar to t() in R

# indexing using arrays;
x = np.random.randn(7, 3)
print(x)
print(x[[1,3, 5]] ) # rearrange the order of display
#====================================
# update ndarray elements
#====================================
# for can assign value as multi-dimensional array or as scalar
# copy vs. view (see previous example)
# batch replace values in an array based on a condition
x = np.random.randn(7, 3)
letters = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
x[letters == 'a'] = 0
print(x)

x = np.random.randn(4, 4)
print(np.where(x > 0, 2, x))

#====================================
# cross array operations
#====================================
x= np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
z = np.array([True, False, True, True, False])
result = [(a if c else b)  for a, b, c in zip(x, y, z)]
print(result)
result = np.where(z, x, y)


