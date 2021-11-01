# strings --
    # -- are bits of text
    # -- can be defined as anything betweem quotes

astring = 'Hello world!'

# prints out 12, because it is 12 characters long, including punctuation and spaces
print(len(astring))

# prints out 4, because the location of the first occurence of the letter 'o' is 4 characters away from the first character 
print(astring.index('o'))

# prints 3 because that is the amount of letter l's in the string
print(astring.count('l'))

# prints a slice of the string starting at index 3 and ending at index 6 (because python is 0-based)
print(astring[3:7])

# prints out 'e', the single character at that index
print(astring[1])

# prints out 'Hello wo', a slice from the start to index 7
print(astring[:7])

# prints out 'world!', a slice from index 6 to the end 
print(astring[6:])

# prints 'ld!', a slice from the 3rd to last index to the end
print(atring[-3:])

# prints 'l ol' -- 
    #  -- the characters from 3 to 7 skipping one character
    #  -- general form is [start:stop:step]
print(astring[3:10:2])

# reverses the string  
print(astring[::-1])

# to uppercase
print(astring.upper())

# to lowercase
print(astring.lower())

# prints true
print(astring.startswith('Hello'))

# prints false
print(astring.endswith('asdfasdfasdf'))

# prints ['Hello', 'world!'] -- 
    #  -- splits the string into a list of strings 
    #  -- in this example at a space
print(astring.split(' '))
