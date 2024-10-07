# ITP 115 , Summer 2024
# Assignment 2
# Name: Ligia Erazo
# Email: lmerazo@usc.edu
# Section:
# Description:
# This program creates variables, gets user input, and displays information to the user.


user_name = input("Enter username: ")
pepperoni_pizza = input("Enter number of Pepperoni Pizza you would like to order: ")
veggie_pizza = input("Enter number of Veggie Pizza you would like to order: ")
lemonade = input("Enter number of Lemonade you would like to order: ")
soda = input("Enter number of Soda you would like to order: ")


pepperoni_pizza = int(pepperoni_pizza)
veggie_pizza = int(veggie_pizza)
lemonade = int(lemonade)
soda = float(soda)

print("\n")
print("Menu")
print("Pepperoni Pizza: $12")
print("Veggie Pizza: $11")
print("Lemonade: $5")
print("Soda: $4.70")
print("Tax and Tips : 10% of the total cost.")

total_cost = pepperoni_pizza + veggie_pizza + lemonade + soda
tax_tips = (pepperoni_pizza + veggie_pizza + lemonade + soda )* .10
final_cost = total_cost + tax_tips
tax_tips = float(tax_tips)
total_cost = float(total_cost)

print("Hello my name is" , user_name + ". I would like to order" , pepperoni_pizza , "Pepperoni Pizza" , veggie_pizza , "Veggie Pizza" , lemonade , "Lemonade and" , soda , "Soda. I believe my total cost is $" , total_cost , "." , "After the tax and tips, can you charge my card $" , final_cost , "? Thank you!")
