import sys
# Asks for a username.

name = input("what is your name: ")

if len(name) > 12:
    print("Your name cannot be more than 12 try again")
    sys.exit()

elif " " in name:
    print("there cannot be space in your name")
    sys.exit()

elif not name.isalpha():
    print("there cannot be digits in your name")
    sys.exit()
else:
    print("Welcome, name verified")

# Asks for the user's age.
age = int(input("how old are you: "))
if age < 16:
    print("you are too young to sign up")
    sys.exit()

else:
    print("Age verified")

# Asks for three subject scores.
math = float(input("ENTER YOUR MATH SCORE"))
economics = float(input("ENTER YOUR ECONOMICS SCORE"))
accounting = float(input("ENTER YOUR ACCOUNTING SCORE"))

# Calculate total
total = math + economics + accounting

# Calculate average
average = (math + economics + accounting) / 3

# Calculate Highest score
if math >= economics and math >= accounting:
    highest = economics
# can also use the max()   eg highest = max(math, economics, accounting)

elif economics >= math and economics >= accounting:
    highest = economics

else:
    highest = accounting

# Calculate lowest score
# can also use if elif else but i am using min()

lowest = min(math, economics, accounting)

# determine the grades of economics
if economics >= 70:
    eco_grade = "A"

elif economics >= 60 and economics <= 69:
    eco_grade = "B"

elif economics >= 50 and economics <= 59:
    eco_grade = "C"

elif economics >= 40 and economics <= 49:
    eco_grade = "D"

else:
    eco_grade = "F"

# determine the grades of math
if math >= 70:
    math_grade = "A"

elif math >= 60 and math <= 69:
    math_grade = "B"

elif math >= 50 and math <= 59:
    math_grade = "C"

elif math >= 40 and math <= 49:
    math_grade = "D"

else:
    math_grade = "F"

# determine the grades of accouting
if accounting >= 70:
    acc_grade = "A"

elif accounting >= 60 and accounting <= 69:
    acc_grade = "B"

elif accounting >= 50 and accounting <= 59:
    acc_grade = "C"

elif accounting >= 40 and accounting <= 49:
    acc_grade = "D"

else:
    acc_grade = "F"

#
status = "PASS" if average >= 50 else "FAIL"

comment = "Excellent student" if average >= 80 else "Good" if average >= 60 else "Better luck next exam"

# Neat report card
print(f"_____STUDENT REPORT CARD_____\n")
print(f"Student Name: {name}")

print(f"Mathematics: {math}: {math_grade}")
print(f"Economics: {economics}: {eco_grade}")
print(f"english: {accounting}: {acc_grade}")

print(f"Average: {average}")
# print(f"Grade: {math_grade}")
# print(f"Grade: {eco_grade}")
# print(f"Grade: {acc_grade}")
print(f"Status: {status}")
print(f"Comment: {comment}")


# Authored by Aliyu.