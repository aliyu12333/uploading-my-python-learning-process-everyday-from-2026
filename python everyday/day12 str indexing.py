# String = accessing elements of a sequence using [] (indexing operator)
#                 [start : end : step }

credit_card = "1234567890"
#for a specific character or number in a position  is just the position of the character or number and teh first position if 0
# print(credit_card[2])
#for character to its end you just put the position and : like this [4:] meaning form position 4 to end eg
#print(credit_card[2:])
#for everything in front or before a position is like this [:3] eg
#print(credit_card[:5])
#for a position through to another position is like this [3:6] eg
#print(credit_card[2:6])
#we can also negative index like this [-8] we use to it to access character from the back like the last character is -1 the second to the last is -2 and so on
#print(credit_card[-1])


# practical use case
last_digit = credit_card[-4:]
print(f"XXX-XXX-{last_digit}")

# Authored by Aliyu