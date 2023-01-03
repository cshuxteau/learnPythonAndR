### Python List

# In Python, a list is an mutable sequence type. They are defined using []
# instead of square brackets () like tuple

# While Python list can contain multiple data types of elements, it is a common practice to store the same data type elements
# in List and different but read only elements in tuple

# difference than R
# Tuple in python is similar to Vector and List in R as tehy are all collections of elements
# Python tuples are not mutable,  R's vectors and lists are mutable
# For Mutable collection object in Python, see List
# tuple is great for read-only object access after creation. it performs better than the mutable objects

#====================================
# create a list
#====================================
x =  [1, 2, 3, 4, 5];
print(x);

y = ["apple","banana", "cherry" ];
print(y);
print(type(y))

x = list(y);  # create a list from another list; similar to list.copy()
print(str(x));

z = ["jan", "feb", "march", True, False, 1, 2]; # you can mix data types
print(z);
print(type(z))

x = ["mouse", [8, 4, 6], (1, 2, 3), ["cat","dog"]]
print(x)

a = [28];  # it is a list
print(type(a));

a = [28,] # it is also a list
print(type(a));

# create empty tuple
a = list();
b = [];

print(type(a));
print(type(b));

x = list(y)
print(x);

#====================================
# access elements of the list
#====================================
# how to access list elements by indices and slicing a segment
# R vector/List index starts with 1, Python starts at 0
# Negative index means different things for Python and R
# Python is for reverse counting
# R is for exclusion
# R indices are inclusive
# Python indices are exclusive (up to, but not include the upper bound)
x = [1, 2, 3, 4, 5, 6, 7, 8]
print(x[1])   #return an individual element of Int (2)
print(x[-1])  #print last element
print(x[:-7]) #print the first element
# slicing returns a tuple
print(x[1:4]) #return a list of 3 elements; the upper bound is excluded
print(x[:])
print(x[-2:-1]) # return only one element, but the result is a tuple  (7,)
print(x[0:2] + x[4:5])  # returns 1, 2, 5 Similar to R x[c(1:3, 6:8)]
# stepped slicing; no build in R method, you have to create an index sequence to accomplish this
print(x[0:5:2] )
print(x[::2])

x = ["mouse", [8, 4, 6], (1, 2, 3), ["cat","dog"]]
print(x[1][1])  # nested list: print the 2nd child element of the 2nd List element

#====================================
# Modify a list: Python List update and R list update are similar
#====================================
x = [1, 2, 3, 4, 5, 6, 7, 8]
x[1] = 10  # 'tuple' object does not support item assignment
print(x)
x[0:3] = [10,20, 30]
print(x)
x[0:1] = [100,200,300]  # update and insert
print(x)

#====================================
# append tuple objects using "+"
#====================================
# In R, you use c() or append()
a = [1, 2, 3]
b = [4, 5, 6]
# Concatenate the tuples using the + operator
c = a + b
print(c)
print(len(c))

# This does not work for List. only works for tuple
# c = sum((a, b), ())
# print(c)
# print(len(c))

# append
c.append(7)
# c.append(7, 8, 9)  # this does not work.  but you can replace element by more elements (see above)
print(c)

c.append([100,101])  # only append one more element [100,101]
print(c)

# insert
c.insert(0, 0)
print(c)

# extend
c.extend(a)
print(c)

d = c.copy();
print(d);
#====================================
# delete elements from list
# There are several ways to delete values from an existing Python list: remove, pop, del, and clear methods.
#====================================
x = ["apple", "banana", "cherry", "kiwi", "orange"];
# Delete the first element of the tuple using the tuple() and list comprehension function
x.remove("apple")
# Print the new tuple
print(x)

x.pop(3)  #remove element at index 3
print(x)

del x[0]  # delete specific element, similar to pop

x.clear() #clear all elements

del x #delete the entire list variable, similar to rm() in R

#====================================
# other key methods
#====================================
# min/max/sum/length/sort
x = [1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2]
print(min(x))
print(max(x))
print(sum(x))
print(len(x))
x.reverse()
print(x)
x.sort()
print(x)

# this won't work due to the mixed object type
# x = ["mouse", [8, 4, 6], (1, 2, 3), ["cat","dog"]]
# x.sort()
# print(x)

#====================================
# Application: find the number of occurrences for an element
#====================================
x = ['a', 'p', 'p', 'l', 'e']
print(x.count('p'))  # prints 2 for occurrance of p; similar to length(which()) in R
print(x.index('l'))  # prints 3 as the first index; similar to which command in R

print('C' in x)  # False
print('p' in x)  # True

# function which returns true if given element is found in tuple
def searchElement(given_list, element):
    # using for loop to traverse the tuple
    for value in given_list:
        # if the given element is equal to the value then return true
        if(value == element):
            return True
    # if the element is not found in tuple then return False
    return False
# given element
element = 'a'
# passing tuple and element to searchElement function
if(searchElement(x, element)):
    print("The item is found in the list")
else:
    print("The specified element does not exist in the list")

#====================================
# Application: select elements based on specific condition
#====================================
# you can accomplish this using count(element) or index(element) or "in" in Python
x = [1, 2, 2, 2, 3, 4, 5, 5, 7, 7, 8, 9, 12, 12, 13, 4, 6, 2]
# count of 2 in tuple
x.index(1)

# use a list comprehension. A list comprehension is a concise way to create a list using a single line of code.
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
# vector arithimatic operation;
# the same approach works for tuple
#====================================
x = [1, 2, 3, 4, 5]
print(x*2)  #extend the list by repeating itself
#====================================
# cross tuple operation
#====================================
# Create two lists of integers
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
# Use a list comprehension to add the elements of the lists together
sum_list = [i + j for i, j in zip(x, y)]
# Print the sum list
print(sum_list)


# use the lamda map method for list
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
# Use the map() function to add the elements of the lists together
sum_list = list(map(lambda i, j: i + j, x, y))
# Print the sum list
print(sum_list)



#====================================
# Element wise operation: apply to both python tuple and list
# similar to sapply in R
#====================================
# use list comprehension
x = ["apple", "orange", "kiwi", "banana", "chrry"]
print("The original list is : " + str(x))
# operations on each list element
# using list comprehension
# uppercasing each element
y = [i.upper() for i in x]
print( str(y))
#use map method
y = list(map(str.upper, x))
print( str(y))

for i, element in enumerate(x):   #use enumerator
    x[i] = element.upper()
print(str(x))

#====================================
# Some advanced cases involving List
# Numpy would be a good alternative
#====================================

from decimal import Decimal

stocks = [['2012-07-31', '16.00', '16.06', '15.81', '15.84', '13753800', '15.8'],
 ['2012-07-30', '16.15', '16.15', '15.90', '15.98', '10187600', '15.9'],
 ['2012-07-27', '15.88', '16.17', '15.84', '16.11', '14220800', '16.1'],
 ['2012-07-19', '15.71', '15.86', '15.64', '15.73', '15985300', '15.7']];

result = [(row[0], Decimal(row[2]) - Decimal(row[3])) for row in stocks]

print(result)