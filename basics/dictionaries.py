# dictionaries are similar to arrays, but with key-value pairs instead of indexes

# each value stored in a dictionary can be accessed using a key, which can be of any data type
phonebook = {}
phonebook['John'] = 938477566
phonebook['Jack'] = 938377264
phonebook['Jill'] = 947662781

# alternative method 
phonebook = {
    'John' : 938477566,
    'Jack' : 938377264,
    'Jill' : 947662781
}

# iterating over dictionaries
for name, number in phonebook.items():
    print('Phone number of %s is %d.' % (name, number))

# removing a value
del phonebook['John']
# OR
phonebook.pop('John')

# exercise -- add 'Jake' to the phonebook with the phone number 938273443 and remove Jill from the phonebook
phonebook = {  
    'John' : 938477566,
    'Jack' : 938377264,
    'Jill' : 947662781
}  
# your code goes here
phonebook['Jake'] = 938273443
del phonebook['Jill']

# testing code
if 'Jake' in phonebook:  
    print('Jake is listed in the phonebook.')
    
if 'Jill' not in phonebook:      
    print('Jill is not listed in the phonebook.')  