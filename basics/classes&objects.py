# objects --
    #  -- are an encapsulation of variables and functions into a single entity
    #  -- get their variables and functions from classes

# classes are essentially a template from which to create your objects

class MyClass:
    variable = 'blah'
    def function(self):
        print('This is a message inside the class.')

# assigning the class to an object
myobjectx = MyClass()

# accessing object variables -- prints 'blah'
print(myobjectx.variable)

# you can create multiple different objects that are of the same class
myobjecty = MyClass()

# however, each object contains independent copies of the variables defined in the class
myobjecty.variable = 'yackity'

# prints 'blah'
print(myobjectx.variable)

# prints 'yackity'
print(myobjecty.variable)

# accessing object functions -- prints 'This is a message inside the class.'
myobjectx.function()
