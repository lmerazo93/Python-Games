# for loops
# range and function - examples

for i in range(3,7):
    print(i)
for j in "hello":
    print(j)


# BELOW WILL CRASH! - Cannot create a loop out of non-sequences.
# print("Now put a for loop inside another.")
 # for i in range(3,7): # outer loop
   # print(i)
   # for j in "hello": # inner loop
        #print(j)

#for k in 100:
    #print(k)
# for l in True:
   # print(l)

# print("length of an integer:" , len(1000)) # object type has NO Length! error.
print("length of an integer:" , len(str(1000))) # turn into string, now it can work.

user_input = input("please enter a username").lower()
while "a" in user_input:
    print("i do not want \"a\" in user input")
    user_input = input("please enter a username").lower()
