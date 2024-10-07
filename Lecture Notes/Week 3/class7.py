## while loops examples - questions with strings

### Ask user some words, create a sentence from these words.
# Hello
# Tommy
# Trojan
# Result: -> Hello Tommy Trojan
### Until user enters "exit".

# while condition:
   # statements

# Step 1: Set initial values
sentence =""
user_input = input("Please enter a word: ")
user_input = user_input.lower()
while user_input != "exit": # if input is not exit then keep asking
    # Step 2: Update your variables:
    sentence = sentence + " " + user_input #update - how?
    print(sentence)
    user_input = user_input.lower()
    user_input = input("Please enter a word: ")
    user_input = user_input.lower()
sentence = sentence + "."
sentence = sentence.replace( "e" ,  "E")
print("my sentence is:" , sentence)