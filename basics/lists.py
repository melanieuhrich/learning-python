# lists --
    # -- are very similar to arrays
    # -- can contain any type of variable 
    # -- can be iterated over

# building a list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
# prints 1
print(mylist[0]) 
# prints 2
print(mylist[1])
# prints 3
print(mylist[2])

# prints out 1, 2, 3
for x in mylist:
    print(x) 

# throws an error
mylist = [1, 2, 3]
print(mylist[10])