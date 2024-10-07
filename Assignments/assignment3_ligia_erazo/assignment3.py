# ITP 115, Summer 2023
# Assignment 3
# Name: Ligia Erazo
# Email: lmerazo@usc.edu
# Section: 31822

print("Select a food item:")
print("a) Aero Chocolate Bar for $1.95")
print("b) Beaver Tail Pastry for $7.25")
print("c) Coffee Crisp for $2.40")
print("d) Dill Pickle Chips for $4.35")



user_input = input("choice: ")
user_input = user_input.lower()

toonies = 200
loonies = 100
quarters = 25
nickels = 5

aero_cost = 195
beaver_cost = 725
coffee = 240
pickle = 435

if user_input == "a":
    print("Good Choice!")
elif user_input == "b":
        print("Good Choice!")
elif user_input == "c":
        print("Good Choice!")
elif user_input == "d":
        print("Good Choice!")
else:
    print("You entered an invalid choice.")
    print("The item selected is the Coffee Crisp.")


print("Payment time!")
toonies_amt = int(input("# of toonies: "))
loonies_amt = int(input("# of loonies: "))
quarters_amt = int(input("# of quarters: "))
nickels_amt = int(input("# of nickels: "))

payment = toonies_amt * toonies + loonies_amt * loonies + quarters_amt * quarters + nickels_amt * nickels

aero_change = payment - aero_cost
beaver_change = payment - beaver_cost
coffee_change = payment - coffee
pickle_change = payment - pickle

if user_input == "a":
    print("Cost is", aero_cost, "cents.")
    print("Payment is" , payment , "cents.")
    if payment >= aero_cost:
        print("You purchased an Aero Chocolate Bar")
        print("Your change is", aero_change)
    else:
        print("You did not enter enough money and will not receive the Areo Chocolate bar")

elif user_input == "b":
    print("Cost is", beaver_cost, "cents.")
    print("Payment is", payment, "cents.")
    if payment >= beaver_cost:
        print("You purchased a Beaver Trail Pastry")
        print("Your change is", beaver_change)
    else:
        print("You did not enter enough money and will not receive the Beaver Trail Pastry")
elif user_input == "d":
    print("Cost is", pickle, "cents.")
    print("Payment is", payment, "cents.")
    if payment >= pickle:
        print("You purchased Dill Pickle Chips")
        print("Your change is", pickle_change)
    else:
        print("You did not enter enough money and will not be receiving the Dill Pickle Chips")
else:
    print("Cost is", coffee, "cents.")
    print("Payment is", payment, "cents.")
    if payment >= coffee:
        print("You purchased a Coffee Crisp")
        print("Your change is", coffee_change)
    else:
        print("You did not enter enough money and will not be receiving the Coffee Crisp")


print("Coins returned.")


