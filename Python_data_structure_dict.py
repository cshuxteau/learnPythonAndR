### Python Dictionary

# A dictionary in Python Programming Language is a container for a set of key-value pairs. The key-value pairs stored
# in a Python Dictionary maintain the insertion order.
# The keys present in a Python dictionary are unique.
# Only immutable object can be stored in dict as keys
# The closest thing to a python dict in R is simply a list or even a R vector. Like most R data types, lists and vectors
# can have a names attribute that can allow lists to act like a set of name-value pairs:

# difference than R
# Tuple in python is similar to Vector and List in R as tehy are all collections of elements
# Python tuples are not mutable,  R's vectors and lists are mutable
# For Mutable collection object in Python, see List
# tuple is great for read-only object access after creation. it performs better than the mutable objects

#====================================
# create a dictionary
#====================================
x = {};
print(x);

y = {"a": "apple","b": "banana", "c": "cherry" };
print(y);
print(type(y))

y = {"a":102456,"b":134567, "c":7892,"d": 8496};
print(type(y))

a = dict(x=5, y=0)
print('numbers =', a)
print(type(a))

a = dict([('x', 5), ('y', -5)], z=8)
print('dict =',a)

c = dict({'x': 4, 'y': 5}, z=8)
print('c =',c)

# zip() creates an iterable
b = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('dict =', b)

# you can construct a dictionary from another dict
x = dict(y)
print(x);

#====================================
# access elements of the dict: use keys
#====================================
# how to access dict elements by key (a.k.a key/value pair)
# In R, you can access element either via key or index; For Python dict, you can only access via Key value, not index
# However, if your key is index, then you can access element via index, but you can't access via negative or range slicing
# therefore, the typical slicing approach you used for Python List and Tuple wont work here
# However you can still use dictionary comprehension to perform some level of slicing
x = {1:102456,2:134567, 3:7892, 4: 8496, 5: 11111, 6:1203, 7:4653 };
print("x[1]", x[1])   #return an individual element of Int (2)
#print(x[-5])  #error: Key error
#print(x[:-7]) #error: Key error
#print(x[1:4]) #error: unhashable type: 'slice'
# print(x[:])  #error: unhashable type: 'slice'

x = {
    "A": 1.1,
    "O": True,
    "M": "HelloWorld",
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "C": 25,
    "T": None,
    "E": ["a", "b", "c"],
    "R": [100, 200, 300, 400]
};

print("nested object inside dict: ", x["B"]["X"]);

# dictionary comprehension
y = ["A", "B", "C"]  # you can also use tuple
z = {key: x[key] for key in x.keys() if key in y}
print("z ", z)

# use list comprehension
y = ["A", "B", "C"]  # you can also use tuple
z = {}
pairs = x.items()
for (key, value) in pairs:
    if key in y:
        z[key] = value
print("z ", z)
#====================================
# Modify a dictionary: modify value
#====================================
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};
x[1] = "x"  # 'tuple' object does not support item assignment
print(x[1]);

x[9] = "z";  # insert a new key
print(x[9]);

x.update({9: 'v'}) # use update method
print(x[9]);

x.update( [(10,"Z")] ); # use update method with a list pair
print(x[10]);

x = {
    "A": 1.1,
    "O": True,
    "M": "HelloWorld",
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "C": 25,
    "T": None,
    "E": ["a", "b", "c"],
    "R": [100, 200, 300, 400]
};

x["R"][3] = 500

print(x)

# append two dictionary to each other using **
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};
y = {'9': 'i'}
z = {**x, **y}
print("z :", z)

# use __setitem__ method; very similar to update(), but with subtle syntax diff
# update takes ONE parameter, hence you have to put your key/value pair in {} or [()]
# but __setitem__ takes 2 parameters: key and value
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};
x.__setitem__(1, "z");
print("x:", x)

#====================================
# append dictionary
#====================================
# In R, you use c() or append(); in Python list and tuple, you can use +; for tuple, you can also use sum()
# this does not work for dict
a = {1:[], 2:[], 3:[]};
b = {4:[], 5:[], 6:[]};
a[1].append("value");  # notice this is NOT append the dict, this is to append a child element to one of the value element
# # Concatenate the tuples using the + operator
# c = a + b
# print(c)
# print(len(c))

# This does not work for Dict nor List. only works for tuple
# c = sum((a, b), ())
# print(c)
# print(len(c))

# combine two dict using **
a = {1:[], 2:[], 3:[]};
b = {4:[], 5:[], 6:[]};
c = {**a, **b}
print("c :", c)

# dict has no append
# c.append([100,100]);

# dict has no insert
# c.insert(0, 0)

# dict has no extend
# c.extend(a)
d = c.copy();
print(d)
#====================================
# delete elements from dict
# There are several ways to delete values from an existing Python list: remove, pop, del, and clear methods.
#====================================
a = {1:[], 2:[], 3:[]};
del a[1];  # delete a key/value pair
del a # delete the entire dict

a = {1:[], 2:[], 3:[]};
a.pop(3)  #remove element with key 3 (similar to List, but not by index)
print(a)

del a[0]  # error if key is not found

a.clear() #clear all elements
#====================================
# other key methods for dict
#====================================
# min/max/sum/length
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};
print(min(x)) # min returns min key
print(max(x)) # min returns max key
print(sum(x)) # min returns sum key
print(len(x)) # len returns pair count
# x.reverse() # no reverse for dict
# x.sort() # no sort for dict
print(sorted(x))  # print a List of keys sorted by key value
print(sorted(x.keys())); # print a List of keys sorted by key value
print(sorted(x, key=x.__getitem__))  # sort by value (notice they need to be the same data type)  <reverse=True>
#====================================
# Application: find the key value in a dict
#====================================
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};

# Dict can't have duplicate keys. there is no OOB count method
# print(x.count('p'))  # prints 2 for occurrance of p; similar to length(which()) in R
# print(x.index('l'))  # prints 3 as the first index; similar to which command in R

print(1 in x)  # true
print(10 in x)  # false

# function which returns true if given element is found in dict key using loop
def searchElement(given_list, element):
    # using for loop to traverse the tuple
    for value in given_list:
        # if the given element is equal to the value then return true
        if(value == element):
            return True
    # if the element is not found in tuple then return False
    return False
# given element
element = 1
# passing tuple and element to searchElement function
if(searchElement(x, element)):
    print("The key is found in the dict: " , element, " value: ",  x[element])
else:
    print("The specified element does not exist in the dict")


#====================================
# Application: sort dict
#====================================
# method 1: using loops
x = {'key5': 'value5', 'key3': 'value3', 'key1': 'value1', 'key2': 'value2'}
y = {}

# sort the keys and store them in a new variable
sorted_value = sorted(x.keys(), reverse=True)
print(str(sorted_value))

# loops through all key values in sorted order
for i in sorted_value:  # i is the sorted key value
   # match the key element with un-sorted dictionary
   for key, value in x.items():
       if key == i:
          # when matched place the key and value in the new dict
          y[key] = value
print(y)

# lambda annoymous function using key function for sorted()
x = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'}
# Sort based on item[0] i.e. key in the dictionary
y = dict(sorted(x.items(), key=lambda n: n[0]))
# Check type of the new dictionary
print(str(y))


# sort using zip method
x = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'}
# create (value, key) pairs using zip()
y = dict(sorted(zip(x.keys(), x.values())))
print(type(y))

# sort using dictionary lamda
x = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'}
y = {}
for key, value in sorted(x.items(), key=lambda item: item[0]):
    # store the sorted items in new dictionary
    y[key] = value
print(str(y))


#====================================
# Application: select elements based on specific condition
#====================================
# use a dict comprehension to find a subset of the dict
x = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'}
filtered_keys = ['key1', 'key2', 'key99']
y = {k:v for k,v in x.items() if k in filtered_keys}
print(y)

# use the lambda anonymous function and the filter() function to find all the elements meet the criteria
x = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'};
filtered_keys = filter(lambda i: i > "key2", x.keys())
# Print the filtered list
y = {k:v for k,v in x.items() if k in filtered_keys}
print(y)

# use a dict comprehension to find a subset of the dict
x = {'key1':1, 'key2':2, 'key3':3}
y = {'key1':1, 'key2':2}
print({ k:x[k] for k in y.keys()})


#====================================
# dictionary arithimatic operation;
# the same approach works for tuple
#====================================
x = {1:"a", 2:"b", 3: "c",  4 : "d", 5 : "e", 6 : "f", 7:"g", 8:"h"};
print(x.keys()*2)  #return a list with repeated key values
#====================================
# cross dictionary operation
#====================================
# merge two dictionaries
x = {'a': 4, 'b': 9, 'c': 10}
y = {'b': 4, 'c': 9, 'd': 12}
z = x.copy()

for key, value in y.items():
    z[key] = value
print(z)

