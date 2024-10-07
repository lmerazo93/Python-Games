num_bottles = 10

while num_bottles > 0: # 10 > 0 -> True until 0 > 0 because it is False
    print(num_bottles, "bottles of tea on the wall")
    print("take one down, pass it around")
    num_bottles -=1
    print(num_bottles, "bottles of tea on the wall")
print("tea is all gone!")

# Motivation 2: Input Error

user_name = input("Enter username: ")
password = input("Enter password: ")
# give access if username is Tommy and password is 1234
while answer.lower() != "tommy" and password !="1234"
    # we want to enter the loop when Access is Denied.
    #user_name is not tommy or password is not 1234
    print("Access Denied. Try again.")
    # Infinite loop: condition is always true. below is the fix
    user_name = input("Enter username: ")
    password = input("Enter password: ")
print("Access Granted. Hello Tommy!")