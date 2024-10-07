# for loops
# range function
# discussion of sequences/iterables

import random

### generate random numbers between 0 and 10 (inclusive)
### add numbers until random number is 7.

total = 0 #initialization
random_number = random.randrange(0,11)
while random_number != 7: # returns True when number is not 7.
    total += random_number
    random_number = random.randrange(0, 11)

print("End of loop. Total value is:" , total)

### for loop examples
for new_var in range(3,13,3):
    print("My number is:" , new_var)
for i in range (0, 50, 5):
    print(i, end=", ")
print(50)

# can we start at a bigger number and go down to a smaller number? Can we take negative steps?

for i in range (50, 0, -5):
    print(i, end=", ")
print(0)

for catdog in "I am a string.": # "I" , " " , "a" , " " , "m" etc..
    print(catdog, end="!")

print() # gives you new line by default

print("Length of seq1: ", len(range(2,7,2))) # 2, 4, 6
print("length of seq2:", len(range(50,43,-2))) # 50, 48, 46, 44

## membership operator - in operator
if "a" in "Hello world":
    print("first option")
elif "e  o" in "Hello World": # no
    print("second option")
elif "HE" in "Hello World": # no because uppercase and lowercase matters
    print("second option")
else:
    print("no membership.")

boolean_variable = 2 in range(0,6) # 0,2,4
print(boolean_variable) # TRUE

boolean_variable = 3 in range(0,6, 2) # 0,2,4
print(boolean_variable)