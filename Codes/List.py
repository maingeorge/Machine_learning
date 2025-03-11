
# List Type

mylist=[] # empty list: Lists are created using square bracket
print(mylist)

# Characteristics of List

#- List items are ordered, changeable, and allow duplicate values.
#- List items are indexed, the first item has index [0], the second item has index [1] etc.
# - When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Since lists are indexed, lists can have items with the same value
# 


names=["Jeff", "Bill", "Steve", "Mohan"] # string list
print(names)

item=[1, "Jeff", "Computer", 75.50, True] # list with heterogeneous data
print(item)


# Access List Values using Indexes

names=["Jeff", "Bill", "Steve", "Mohan"] 
print(names[0]) # returns "Jeff"
print(names[1]) # returns "Bill"
print(names[2]) # returns "Steve"
print(names[3]) # returns "Mohan"
print(names[4]) # throws IndexError: list index out of range

# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# From Python's perspective, lists are defined as objects with the data type 'list':

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Access List Items

# List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# By leaving out the start value, the range will start at the first item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items. The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)






























