# 1. Show the text
# 2. Show a specific character
# 3. Show part of the text
# 4. Reverse the text
# 5. Replace a character
# 6. Convert to uppercase
# 7. Convert to lowercase
# 8. Count the characters
# 9. Enter new text
# 10. Exit

import sys
text = input("enter texts or characters: ")
if len(text) >= 13:
    print("cannot handle more than 12 character text, try again ")
    sys.exit()

# print(text[0:1])
# print(text[0:2])
# print(text[0:3])
# print(text[0:4])
# print(text[0:5])
# print(text[0:6])
# print(text[0:7])
# print(text[0:8])
# print(text[0:9])
# print(text[0:10])
# print(text[0:11])
# print(text[0:12])

user_position = input("enter a position to find a character that is there: ")
if user_position == "0":
    print(text[0])

elif user_position == "1":
    print(text[1])

elif user_position == "2":
    print(text[2])

elif user_position == "3":
    print(text[3])

elif user_position == "4":
    print(text[4])

elif user_position == "5":
    print(text[5])

elif user_position == "6":
    print(text[6])

elif user_position == "7":
    print(text[7])

elif user_position == "8":
    print(text[8])

elif user_position == "9":
    print(text[9])

elif user_position == "10":
    print(text[10])

elif user_position == "11":
    print(text[11])

elif user_position == "12":
    print(text[12])

#Show parts of text

print(text[0:1])
print(text[0:2])
print(text[0:3])
print(text[0:4])
print(text[0:5])
print(text[0:6])
print(text[0:7])
print(text[0:8])
print(text[0:9])
print(text[0:10])
print(text[0:11])

# Replace a character

print(text.replace(" ", "-"))

# Reverse the text
print(text[::-1])

# Convert to uppercase

print(text.upper())

# Convert to lowercase

print(text.lower())

# Count the characters
print(len(text))


#Authored by aliyu