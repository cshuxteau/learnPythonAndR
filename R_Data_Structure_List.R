
### R List

# In Python, a list is a collection of values that can be of any data type, including other lists. 
# Both R and Python Lists are ordered and changeable, and allow you to store multiple values in a single data structure.


# difference than Python
# List in R are similar to tuples in Python in that they are collections of elements 
# it's important to note that R lists are more flexible than Python lists, as they can contain elements of different data types, 
# while Python lists can only contain elements of the same data type.
# both python list and R Lists are mutable. (unlike tuple in Python) 

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
# create a list
#====================================
x <- list(1, 2, 3, 4, 5)  
print(x)
y <- list("apple", "banana", "cherry") 
print(y)
#mixed data types
z <- list(1, 2, 3, "apple", "banana", TRUE, FALSE )  
print(z)
# nested data types
a <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)
print(a)

# create list with named element
x <- list(A = 1:5,                              
          B = 6:10,
          c = LETTERS[15:19])
x$A

x <- list(c(1:10)) # this list only has 1 element,  not 10
length(x)

x <- list(seq(1:10)) # this list only has 1 element,  not 10
length(x)

#====================================
# name list elements (this is unique to R)
# In Python, lists do not have a built-in way to assign names to their elements.  
# However, you can achieve a similar effect by using a dictionary, which is a data structure 
# that maps keys (names) to values.
#====================================

# Create a list containing a vector, a matrix and a list.
x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
                  list("green",12.3))

# Give names to the elements in the list.
names(x) <- c("1st Quarter", "A_Matrix", "B Inner list")

# Show the list.
print(x)
x$`1st Quarter`


#====================================
# access elements of the list
#====================================

# how to access vector by indices and slicing
# R vector index starts with 1, Python starts at 0
# the codes below is almost identical for R Vector
x <- list(1, 2, 3, 4, 5, 6, 7, 8)
x[1]
x[1:3]
x[c(1,3,5)]
x[c(1:3, 6:8)]
# steps: python has a direct method to accomplish this; 
# R has to leverage seq function
t_index <- seq(1,8, 2)
x[seq(1,8, 2)]

# this is unique for R List. It is different from Python and R Vector
# use element names to access individual elements by $
x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
          list("green",12.3))

# Give names to the elements in the list.
names(x) <- c("1st Quarter", "A_Matrix", "A Inner list")
x$`1st Quarter`
x$`A_Matrix`

#====================================
# modify a list elements. mutable'
# Python tuple is not mutable, but python list is mutable
#====================================
# the code below is the same for R List and R vector
x <- list(1, 2, 3, 4, 5, 6, 7, 8)
x[1] <- 10
x
x[c(1,3,5)] <- c(10, 20, 30)
x

# this code is unique to R List
x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
          list("green",12.3))
x[[1]] <- c("January", "Feburary", "March")
names(x) <- c("1st Quarter", "A_Matrix", "A Inner list")
x$`A_Matrix` <- matrix(c(1:8), nrow = 2)
x[[2]]

#====================================
# append list + Unlist to flat out the list structure into a vector
#====================================
x <- list(1, 2, 3)
y <- list('a', 'b', 'c')

# Combine the lists into a single list
Z <- c(x, y)
# Print the combined list
z

z <- list(NA)
z <- append(x, y)
z

# Unlist will return a vector of list elements
unlist(z)

( x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
            list("green",12.3))  )
unlist(x)

#====================================
# delete elements from list
#====================================
# this code is the same for R vector
x <- list("apple", "banana", "cherry", "kiwi", "orange")
#remove specific elements from vector
( x <- x[! x %in% c('apple', 'banana')] )

x <- list(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
#remove 1, 4, and 5
( x <- x[! x %in% c(1:4, 7:8)] )

x <- list(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
( x <- x[!(x < 3 | x > 10)] )

# remove duplicates
x <- list(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13)
( x <- x[!duplicated(x)] )


#====================================
# other key methodsfor R List
#====================================
# Notice: there is no min/max/order for List as it is becaue it is a nested data structure
# to achive the same results, you can use unlis to turn list structure into a vector
# sort by element names
x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
          list("green",12.3, NA, 3, 9, "Feb"))
names(x) <- c("1st Quarter", "A_Matrix", "A Inner list")
x[order(names(x))]  # sorted by the name values; not the actual values of elements
# get the min/max values from list
max(unlist(x))
min(unlist(x))
min(unlist(x), na.rm=TRUE) # remove NA before compare values. otherwise, NA will be the min
length(x)  # count elements, not the specific values since list is a nested data structure in R
unique(x)  # while it 

min(x)
max(x)
sum(x)
length(x)
sort(x) # ascending order
unique(x) # the result is not likely to be where you expect. Again, you can use unlist to get the unique element values

#====================================
# Applicatio: find the number of occurrences for an element
#====================================
# you can accomplish this using count(element) in Python
x <- list(1, 4, 3, 2, 2, 3, 2)
# count of 2 in vec
print(length(x[x == 1]))
print(length(which(x == 2)))

#====================================
# Application: select elements based on specific condition
#====================================
# you can accomplish this using count(element) in Python
x <- list(1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2)
# count of 2 in vec
which(x == 2 )  ## return indices
x[x != 2]
x[ x > 3]

x <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
          list("green",12.3, NA, 3, 9, "Feb"))
which(x > 0  )  ## error: 'list' object cannot be coerced to type 'double'

#====================================
# list arithmetic operation
#====================================
# very different than vector because list is a hierarchical object; it has mixed data types
x <- list(1,2,3,4,5,6,7,8,9,10)
( x + 1  ) # error:in x + 1 : non-numeric argument to binary operator 
Reduce("+",x)  # this gives you an aggregated result by summarizing all elements in the list
# element wise operation using sapply / 
# Use sapply() 
sapply(x, function(x) (x + 1) )  # return a vector

# You can also use the lapply() function to perform a mathematical operation on the elements of a list. 
# This function is similar to sapply(), but returns a list of the results rather than a vector.
lapply(x, function(x) (x + 1) ) # return a list

# use additional lib
library(purrr)
map(x, function(x) x^2)  # return a list

# more advanced functions 
add <- function(x) Reduce(`+`, x)
add(x)

#====================================
# cross list operation
#====================================
(x <- list(1, 2, 3, 4, 5))
(y <- list(10, 20, 30, 40, 50))

# Use Map() to add the elements of the lists together
Map(function(x, y) x + y, x, y)


