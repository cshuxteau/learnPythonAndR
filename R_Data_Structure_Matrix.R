### R matrices

# In Python, numpy package ndarray is a multidimentional array that is the closest counterpart of the R Matrix  
# Matrices are the R objects in which the elements are arranged in a two-dimensional rectangular layout. 
# They contain elements of the same atomic types, typically numeric values

# difference than Python
# python array (numpy array) does not have row/col names.  to do that, you can use panda dataframe
#====================================
# restart/reset the sample
#====================================
rm(x)
rm(y)
rm(z)
rm(mat)

#====================================
# create a matrix
#====================================
x <- matrix(c(1, 2, 3, 4, 5,6), nrow = 3, byrow = T, dimnames = list(c("r1", "r2", "r3"),NULL ) ) 
print(x)

y <- matrix(c(1, 2, 3, 4, 5,6), nrow = 3, byrow = T, dimnames = list(c("r1", "r2", "r3"), c("c1","c2") ) ) 
print(y)

#mixed data types will convert every element to be a char
z <- matrix(c(1, 2, 3, 4, 5, "A"), nrow = 2, byrow = F, dimnames = list(c("r1", "r2"), c("c1","c2", "c3") ) ) 
print(z)

#create empty matrix
x = matrix(nrow = 3, dimnames  = list(c("r1","r2", "r3"), NULL) )
print(x)
x = matrix(ncol = 3, dimnames  = list(NULL, c("C1","C2", "C3")) )
print(x)

#use CBind or RBind
mat.data1 <- c(1,2,3)
mat.data2 <- c(4,5,6)
mat.data3 <- c(7,8,9)
mat <- cbind(mat.data1,mat.data2,mat.data3)
print(mat)

# create matrix by changing vector dimension
x <- c(1, 2, 3, 4, 5,6)
dim(x) <- c(2, 3)
print(x)

#====================================
# name matrix by rows and/or columns (this is unique to R)
# In Python, numpy does not have a built-in way to assign names to their elements.  
#====================================

# Create a list containing a vector, a matrix and a list.
x <- c(1, 2, 3, 4, 5,6)
dim(x) <- c(2, 3)
rownames(x) <- c("r1","r2")
print(x)

#====================================
# access elements of the list
#====================================

x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8), nrow = 4, byrow = T, dimnames=list(c("r1","r2","r3","r4"),c("c1","c2" )))
print(x)
x[1,]
x[1:3,]
x[c(1,2,4),]
x[, 1:2]
x[1, 2]
x[-1,]
x[, -1]

# use rowname, colname
x["r1",]
x[, "c1"]

# If we select a single row or column this way, the result is a vector and not a matrix. 
# We can use the drop=FALSE argument to avoid this behavior. The result will still be a matrix
x[, "c1", drop = FALSE]

x[c(TRUE, FALSE, TRUE, FALSE),]

# select data element based on certain conditions
which(x%%2!=0, arr.ind = T)

# use apply function
apply(x>1, 1 ,which.max)

# use matrix selector
x[x[,"c1"]==3,]


#====================================
# modify a matrix
# similar to ndarray in Python
#====================================
# the code below is the same for R List and R vector
x <- matrix(c(1, 2, 3, 4, 5,6, 7, 8), nrow = 4, byrow = T, dimnames = list(c("r1", "r2", "r3", "r4"),NULL ) ) 
print(x)
x[c(1), ] <- c(2,1)
print(x)

x[x%%2!=0] <- -1 #elements not divisible by 2 are relaced with 1
print(x)

x[1,2]<- 3

tmax <- t(x)
print(tmax)
dim(tmax)
#====================================
# matrix arithematic operation
#====================================
x <- matrix(c(1, 2, 3, 4, 5,6, 7, 8), nrow = 4, byrow = T, dimnames = list(c("r1", "r2", "r3", "r4"),NULL ) ) 
# matrix element wise operation
y <- x + 10
print(y)
print( x * y )

x <- matrix(c(10, 8,
              5, 12), ncol = 2, byrow = TRUE)
x

y <- matrix(c(5, 3,
              15, 6), ncol = 2, byrow = TRUE)

x %*% y
crossprod(x, y)

diag(4)



#====================================
# Array in R
# Array in R are similar to matrices but can have more than two dimensions. An array is created using the array() function. 
# It takes vectors as input and uses the values in the dim parameter to create an array.
# this is similar to Numpy Array, dim is similar to Shape in Python: 
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], shape=(3, 3))
#====================================

# Create two vectors of different lengths.
x <- c(5,9,3)
y <- c(10,11,12,13,14,15)

# Take these vectors as input to the array.
z <- array(c(x,y),dim = c(3,3,2))
print(z)
