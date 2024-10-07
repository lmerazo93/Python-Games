# ITP 115, Summer 2023
# Lab 4
# Name: Ligia Erazo
# Email: lmerazo@usc.edu
# Section: 31822
# Description: For Loops


user_input = input("Enter phrase 1 (q or Q to exit):")
phrase_no = 1
while user_input.upper() != "Q":
    changed = 0
    modified_phrase =""
    for i in user_input:
        if i == "A":
            modified_phrase += "4" #concat 4 string to your modified phrase
            changed += 1
        elif i == "I":
            modified_phrase += "1"
            changed += 1
        elif i == "E":
            modified_phrase += "3"
            changed += 1
        elif i == "i":
            modified_phrase += "1"
            changed += 1
        elif i == "5":
            modified_phrase += "S"
            changed += 1
        elif i == "1":
            modified_phrase += "!"
            changed += 1
        else:
            modified_phrase += i

    print("Your modified phrase " + str(phrase_no) + " is " + modified_phrase)
    print("changed " + str(changed) + " characters")

    phrase_no += 1


    user_input = input("Enter phrase " + str(phrase_no) + "(q or Q to exit):")

print("Thank you!")

