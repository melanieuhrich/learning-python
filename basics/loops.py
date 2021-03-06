# the 'for' loop iterates over a given sequence 
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# the range function returns a new list with numbers of that specified range and is 0-based
# prints 0, 1, 2, 3, 4
for x in range(5):
    print(x)
# prints 3, 4, 5
for x in range(3, 6):
    print(x)
# prints 3, 5, 7
for x in range(3, 8, 2):
    print(x)

# the while loop repeats as long as a certain boolean condition is met
# prints 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count += 1

# a 'break' statement is used to exit a loop
# prints 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# a 'continue' statement is used to skip the current block and return to the 'for'/'while' statement
# prints only odd numbers -- 1, 3, 5, 7, 9, etc.
for x in range(20):
    # check if x is even
    if x % 2 == 0:
        continue
    print(x)

# the 'else' clause --
    #  -- is executed when the loop condition fails 
    #  -- is skipped if a 'break' statement is executed 
    #  -- is executed even if there is a 'continue' statement 

# prints 0, 1, 2, 3, 4 and then prints 'count value reached 5'
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print('count value reached %d' % (count))

# prints 1, 2, 3, 4
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print('this is not printed because the for loop is terminated by break but not due to fail in condition')

# exercise -- 
    #  -- loop through and print out all even numbers from the list in the order they are received 
    #  -- do not print any numbers that come after 237 in the sequence
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if(number % 2 == 0):
        print(number)
    if(number == 237):
        break