answer = input("is the audio better?: ")
answer = answer.upper()
print(answer + answer) # 100 + 100 =100100 (not mathematical)
# input always returns a string variable
# string + string

# what happens if I want to do a mathematical operation like (summation +) ?
# conver to integer:
print(int(answer) + int(answer))
# this will throw an error if user inputs words like "yes" because they cannot convert that to an integer
# perhaps you want to store your input as an integer

print("The \"answer\" is:" + answer + answer)

### MATHEMATICAL OPERATIONS

# is output float or int?
print("Line1:" , 5 + 2.0) # int + float -> output 7.0 will be float
print("Line2" , 4/2) # int/int -> float (2.0) if you use "/" the output will be float
print("Line3" , 4//2) # int//int -> int output (2)
print("Line4" , 4.0/2) # Rule 1: if you use float output will be float
print("Line5" , 4.0//2) # Rule 1: if you use float output will be float

# Excercise
random_number = input("guess a number")
random_number = int(random_number)
# How would you check if this number is even or not?
# even 0 ,2 , 4 ,6 ,8 , 10 , 12 etc..
print("the remainder:" , random_number % 2)
# all even numbers can be divisible by two and should not have a remainder.
# use PEMDAS for mathematical operations
result = ((100+45)*5)/7
# or do this:
summation = 100+ 45
mult = summation * 5
divide = mult/7