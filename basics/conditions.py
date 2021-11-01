# python uses boolean logic to evaluate conditions

x = 2
# prints true
print(x == 2)
# prints false 
print(x == 3)
# prints true
print(x < 3)

# the 'and' and 'or' boolean operators allow for building complex boolean expressions
name = 'John'
age = 23
if name == 'John' and age == 23:
    print('Your name is John and you are 23 years old.')
if name == 'John' or name == 'Rick':
    print('Your name is either John or Rick.')

# the 'in' operator can be used to check if a specified object exists within an iterable object container, such as a list
name = 'John'
if name in ['John', 'Rick']:
    print('Your name is either John or Rick.')

# if statement using code blocks
statement = False 
another_statement = True 
if statment is True:
    # do something
    pass
elif another_statement is True:
    # do something else
    pass 
else: 
    # do another thing
    pass 

# a statement is evaluated as true if one of the following is correct --
    #  -- the 'True' boolean variable is given or caluclated using an expression
    #  -- an object which is not considered 'empty' is passed

# examples of objects which are considered empty --
    #  -- an empty string: ''
    #  -- an empty list: []
    #  -- the number zero: 0
    #  -- the false boolean variable: False

# the 'is' operator does not match the values of the variables, but the instances themselves
x = [1, 2, 3]
y = [1, 2, 3]
# prints true
print(x == y)
# prints false 
print(x is y)

# using the 'not' operator before a boolean expression inverts it
# prints true
print(not False)
# prints false
print((not False) == (False)) 

# exercise -- set the variables so that each statement resolves as True
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1,2]
if number > 15:
    print('1')
if first_array:
    print('2')
if len(second_array) == 2:
    print('3')
if len(first_array) + len(second_array) == 5:
    print('4')
if first_array and first_array[0] == 1:
    print('5')
if not second_number:
    print('6')