### Python Set

# In Python, you can use the set data type to represent a set of unique elements.
# A set is an unordered collection of items, and each item must be unique and immutable (i.e., it cannot be modified).
# A set can be created in two ways: via the set function or via a set literal with curly braces{}

# difference than R
# there is no base object like Set in R; but you can install additional packages to have a similar set function as in Python
#====================================
# create a set
#====================================
x = {1,2,3,4,5 };
print(x);

y = {"a","b","c","d"};
# the order of elements in a set is not preserved. Sets are unordered collections of items, and do not maintain any specific order for the elements.
# if you want to preserve the order, you can use tuple or list
print(y)

a = set()
print('an empty set ', a)

x = set(y) # create set from another set
print("x", x);

x = set([1, 2, 3, 2 ]);  # create a set from a list
print(x)

x = [1, 2, 3, 4]  # create
y = set(x)
print(y)
print(type(y))

x = (1, 2, 3, 4, 2)
y = set(x)
print(y)
print(type(y))
#====================================
# add or remove an element from a set
#====================================
x = set([1, 2, 3]);
print(x)
x.add(1)
x.add(2)
x.add(3)
print(x)
x.add(4)
print(x)
x.update((5,6))  # you can append multiple items using a tuple
y = [7,8]
x.update(y) # you can append multiple items using a list
y = {9,10}
x.update(y) # you can append multiple items using another set
print(x)
y = { 11, 12}
x |= set(y) # use pipe operator
print(x)



# remove an element from the set
x.remove(3)

# print the set
print(x)

#====================================
# access elements of the set
#====================================
x = {1,2,3,4,5};
# check if an element is in the set
print(2 in x)  # prints "True"
print(6 in x)  # prints "False"

for a in x: # iteration
  print(a)


#====================================
# cross set operations
#====================================
# In R, you use c() or append(); in Python list and tuple, you can use +; for tuple, you can also use sum()
x = {1, 2, 3}
y = {6, 7, 8}
# set union
print(x | y)
print(y.union(x))

#set append
x = {1, 2, 3}
y = {6, 7, 8}
x.update(y)
print(x)

x = y.copy();
print(x)


x = {1, 2, 3}
y = {3, 2, 8}
# set intersection
print(x & y)
print(y.intersection(x))

x = {1, 2, 3}
y = {3, 2, 8}

# set difference: in x not in y
print(x - y)
# set difference: in y not in x
print(y.difference(x))

x = {1, 2, 3, 9, 0}
y = {3, 2, 8, 7, 5}
# symetric difference
# The set which contains the elements which are either in set A or in set B but not in both is called the Python symmetric difference between two given sets.
print(x ^ y)
print(y.symmetric_difference(x))
x.symmetric_difference_update(y)  # Set x to contain the elements in either x or y but not both
print(x)
x ^= y
print(x)

print(x.issubset(y));
print(x.issuperset(y));
print(x.isdisjoint(y));


# use zip to pair two sets
for (i1, i2) in zip(x, y):
    print(i1, i2)

#====================================
# Remove an element from a set
#====================================
x = {1,2,3,4,5};
x.remove(1)
x.discard(2)
x.clear()
del(x)

x = {1,2,3,4,5};
a = x.pop();  #remove random element from the set
print(a)

#====================================
# other key methods for set
#====================================
# min/max/sum/length
x = {1,7,2,3,4,5};
print(min(x))
print(max(x))
print(sum(x))
print(len(x))
# x.reverse() # no reverse for dict
# x.sort() # no sort for dict
print(sorted(x))  # print sorted set

#====================================
# Application: enumerate elements in a set
#====================================
x = {1,7,2,3,4,5};

# loop
for item in x:
  print(item)

# enumerate
for counter, item in enumerate(x): # may not be in the original order
  print(counter, ":", item)

# use iter
for item in iter(x): # may not be in the original order
  print(item)

# use for loop
y = list(x)
for i in range(0,len(y)):
  print(y[i])

# use while loop
i = 0
while i < len(x):
  print(y[i])
  i = i + 1

# use comprehension
val = [print(item) for item in x]


#====================================
# Application: select elements based on specific condition
#====================================
x = {1, 2, 3, 4, 5}
# select elements from the set that are greater than 3
selected = [i for i in x if i > 3]
print(selected)  # prints "[4, 5]"
print(type(selected)) # result is a list
print(set(selected))

# select elements from the set that are greater than 3
selected = filter(lambda i: i > 3, x)
print(selected)  # prints "[4, 5]"
print(type(selected))
print(set(selected))

