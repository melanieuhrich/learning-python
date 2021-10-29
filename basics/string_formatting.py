# python uses C-style string formatting -- 
    # -- the % operator is used 
    # -- in conjunction with an argument specifier 

# prints 'Hello, John!'
name = 'John'
print('Hello, %s!' % name)

# to use two or more argument specfifiers, use a tuple (parentheses) 
name = 'John'
age = 23
# prints 'John is 23 years old.'
print('%s is %d years old.' % (name, age))

# an object which is not a string can be formatted using the %s operator as well
mylist = [1, 2, 3]
# prints 'A list: [1, 2, 3]'
print('A list: %s' % mylist)

# basic argument specifiers --
    # -- %s - String (or any object with a string representation, like numbers)
    # -- %d - Integers
    # -- %f - Floating point numbers 
    # -- %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
    # -- %x/%X -- Integers in hex representation (lowercase/uppercase)

# exercise
data = ('John', 'Doe', 53.44)
format_string = 'Hello, %s %s. Your current balance is $%s.'
# prints 'Hello, John Doe. Your current balance is $53.44.'
print(format_string % data)
