### Python Tuple

# In Python, a tuple is an immutable sequence type. This means that once you create a tuple, you cannot change its
# contents by adding, removing, or modifying elements. Tuples are similar to lists, but are defined using parentheses ()
# instead of square brackets [].

# both R vectors and Python tuples can contain multiple data types of elements

# difference than R
# Tuple in python is similar to Vector and List in R as tehy are all collections of elements
# Python tuples are not mutable,  R's vectors and lists are mutable
# For Mutable collection object in Python, see List
# tuple is great for read-only object access after creation. it performs better than the mutable objects

#====================================
# restart/reset the sample
#====================================


#====================================
# create a tuple
#====================================
x =  (1, 2, 3, 4, 5);
print(x);

y = tuple( ("apple","banana", "cherry" ) );  # double parenthesis is important. otherwise, error "tuple expected at most 1 argument, got 3"
print(y);
print(type(y))

z = ("jan", "feb", "march", True, False, 1, 2); # you can mix data types
print(z);
print(type(z))

x = ("mouse", [8, 4, 6], (1, 2, 3))
print(x)

a = (28);  # this is NOT a tuple. it is an Int
print(type(a));

a = (28,) # remember to include ","
print(type(a))

# create empty tuple
a = tuple()
b = ()
c = int()
print(a)
print(b)
print(c)

#====================================
# access elements of the tuple
#====================================
# how to access tuple elements by indices and slicing a segment
# R vector index starts with 1, Python starts at 0
# Negative index means different things for Python and R
# Python is for reverse counting
# R is for exclusion
# R indices are inclusive
# Python indices are exclusive (up to, but not include the upper bound)
x = (1, 2, 3, 4, 5, 6, 7, 8)
print(x[1])   #return an individual element of Int (2)
print(x[-1])  #print last element
print(x[:-7])
# slicing returns a tuple
print(x[1:4]) #return a tuple of 3 elements; the upper bound is excluded
print(x[:])
print(x[-2:-1]) # return only one element, but the result is a tuple  (7,)
print(x[0:2] + x[4:5])  # returns 1, 2, 5 Similar to R x[c(1:3, 6:8)]
# stepped slicing; no build in R method, you have to create an index sequence to accomplish this
print(x[0:5:2] )
print(x[::2])

#====================================
# You can't modify an element of tuple since it is not mutable
# this is different from R vector/list and Python list
#====================================
#x = (1, 2, 3, 4, 5, 6, 7, 8)
#x[1] = 10  # 'tuple' object does not support item assignment

#====================================
# append tuple objects using "+"
#====================================
# In R, you use c() or append()
a = (1, 2, 3)
b = (4, 5, 6)
# Concatenate the tuples using the + operator
c = a + b
print(c)
print(len(c))

# Altnerative way
c = sum((a, b), ())
print(c)
print(len(c))

#====================================
# delete elements from tuple - You can't do it as a mutable object
# however, you still can create another tuple object based on your existing tuple and remove the element you don't need
#====================================
x = ("apple", "banana", "cherry", "kiwi", "orange")
# Delete the first element of the tuple using the tuple() and list comprehension function
new_tuple = tuple([i for i in x if i != "apple"])
# Print the new tuple
print(new_tuple)

# using slicing
# Delete the third element of the tuple using slicing
new_tuple = x[:2] + x[3:]
# Print the new tuple
print(new_tuple)


#====================================
# other key methods
#====================================
# min/max
x = (1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2)
print(min(x))
print(max(x))
print(sum(x))
print(len(x))


#====================================
# Application: find the number of occurrences for an element
#====================================
x = ('a', 'p', 'p', 'l', 'e')
print(x.count('p'))  # prints 2 for occurrance of p; similar to length(which()) in R
print(x.index('l'))  # prints 3 as the first index; similar to which command in R

print('C' in x)  # False
print('p' in x)  # True

# function which returns true if given element is found in tuple
def searchElement(given_tuple, element):
    # using for loop to traverse the tuple
    for value in given_tuple:
        # if the given element is equal to the value then return true
        if(value == element):
            return True
    # if the element is not found in tuple then return False
    return False
# given element
element = 'a'
# passing tuple and element to searchElement function
if(searchElement(x, element)):
    print("The item is found in the tuple")
else:
    print("The specified element does not exist in the tuple")

#====================================
# Application: select elements based on specific condition
#====================================
# you can accomplish this using count(element) or index(element) or "in" in Python
x <- (1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2)
# count of 2 in tuple
x.index(1)

# use a list comprehension. A list comprehension is a concise way to create a list using a single line of code.
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Use a list comprehension to find all the elements in the tuple that are greater than 5
filtered_list = [i for i in x if i > 5]
# Print the filtered list
print(filtered_list)

# use the lambda anonymous function and the filter() function to find all the elements meet the criteria
# In Python, lambda is a keyword that is used to create anonymous functions. An anonymous function is a function
# that is defined without a name, and is typically used as a small, throwaway function.
filtered_list = filter(lambda i: i > 5, x)
# Print the filtered list
print(list(filtered_list))

#====================================
# vector arithimatic operation
#====================================
(x <- c(1, 2, 3, 4, 5))
(x <- x + 1 )  #element wise operations
#====================================
# cross vector operation
#====================================
(x <- c(1, 2, 3, 4, 5))
(y <- c(10, 20, 30, 40, 50))
(x + y )

