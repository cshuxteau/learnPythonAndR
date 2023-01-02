
### vector

# Vectors are the most basic R data objects and there are six types of atomic vectors. 
# They are logical, integer, double, complex, character and raw.
# In R, the equivalent of a Python tuple is a vector. Vectors are one-dimensional arrays 
# that can hold elements of any data type, including character, numeric, and logical data. 
# You can create a vector by enclosing a comma-separated list of values in the c() function. 

# difference than Python
# Vectors in R are similar to tuples in Python in that they are collections of elements 
# Python tuples are not mutable,  R's tuples are mutable 

#====================================
# restart/reset the sample
#====================================
rm(x)
rm(y)
rm(z)
rm(a)
rm(b)
rm(c)
rm(d)

#====================================
# create a vector
#====================================
(x <- c(1, 2, 3, 4, 5))
(y <- c("apple", "banana", "cherry"))
(z <- c(1, 2, 3, "apple", "banana", TRUE, FALSE) )
(a <- vector())
(b <- numeric() )
(c <- c() )
( d <- rep(NULL, 0) )
( a <- append(a,x) )


#====================================
# access elements of the vector
#====================================

# how to access vector by indices and slicing
# R vector index starts with 1, Python starts at 0
x <- c(1, 2, 3, 4, 5, 6, 7, 8)
x[1]
x[1:3]
x[c(1,3,5)]
x[c(1:3, 6:8)]
# steps: python has a direct method to accomplish this; 
# R has to leverage seq function
t_index <- seq(1,8, 2)
x[seq(1,8, 2)]



#====================================
# modify a vector's elements. mutable
#====================================
x <- c(1, 2, 3, 4, 5, 6, 7, 8)
x[1] <- 10
x
x[c(1,3,5)] <- c(10, 20, 30)
x


#====================================
# append vector
#====================================
(x <- c(1, 2, 3, 4, 5))
(y <- c("apple", "banana", "cherry"))
(z <- c(x,y) )
(a <- append(x,y))


#====================================
# delete elements from vector
#====================================
x <- c("apple", "banana", "cherry", "kiwi", "orange")
#remove specific elements from vector
( x <- x[! x %in% c('apple', 'banana')] )

x <- c(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
#remove 1, 4, and 5
( x <- x[! x %in% c(1:4, 7:8)] )

x <- c(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
( x <- x[!(x < 3 | x > 10)] )

# remove duplicates
x <- c(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
( x <- x[!duplicated(x)] )


#====================================
# other key methods
#====================================
# min/max
x <- c(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2)
min(x)
max(x)
sum(x)
length(x)
sort(x) # ascending order
sort(x, decreasing = TRUE) # descending order
unique(x)
unique(sort(x) )

#====================================
# Applicatio: find the number of occurrences for an element
#====================================
# you can accomplish this using count(element) in Python
x <- c(1, 4, 3, 2, 2, 3, 2)
# count of 2 in vec
print(length(x[x == 1]))
print(length(which(x == 2)))

#====================================
# Application: select elements based on specific condition
#====================================
# you can accomplish this using count(element) in Python
x <- c(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2)
# count of 2 in vec
which(x == 2 )  ## return indices
x[x != 2]
x[ x > 3]

#====================================
# cross vector operation
#====================================
(x <- c(1, 2, 3, 4, 5))
(y <- c(10, 20, 30, 40, 50))
(x + y )