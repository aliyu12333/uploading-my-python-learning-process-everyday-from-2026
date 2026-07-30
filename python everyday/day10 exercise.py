# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("ENTER YOUR NAME: ")
result = len(name)
space = name.find(" ")
digit = name.isalpha()


if result > 12:
    print("Your name cannot be more than 12 try again")

elif space != -1:
    print("there cannot be space in your name")

elif digit:
    print("there cannot be digits in your name")

else:
    print("name successfully verified")


# Authored by aliyu