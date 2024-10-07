# ITP 115, Summer 2023
# Assignment 4
# Name: Ligia Erazo
# Email: lmerazo@usc.edu
# Section: 31822
# Description: While Loops



total_integer = 0
sum_integer = 0
total_even_integer = 0
sum_even_integer = 0



print("Even Numbers")
print("Enter an integer (negative number to quit): ")

user_input = int(input("> "))


while user_input > 0:
    total_integer += 1
    sum_integer += user_input

    if user_input % 2 == 0:
        total_even_integer += 1
        sum_even_integer += user_input

    user_input = int(input("> "))



print("The count is: " , total_integer)
print("The sum (total) is: " , sum_integer)
print("The count of even numbers is: " , total_even_integer)
print("The sum (total) of even numbers is: " , sum_even_integer)


total_integer = 0
sum_integer = 0
total_odd_integer = 0
sum_odd_integer = 0



print("Odd Numbers")
print("Enter an integer (negative number to quit): ")

user_input = int(input("> "))

while user_input >= 0:
    total_integer += 1
    sum_integer += user_input

    if user_input % 2 != 0:
        total_odd_integer += 1
        sum_odd_integer += user_input

    user_input = int(input("> "))



print("The count is: " , total_integer)
print("The sum (total) is: " , sum_integer)
print("The count of odd numbers is: " , total_odd_integer)
print("The sum (total) of odd numbers is: " , sum_odd_integer)





