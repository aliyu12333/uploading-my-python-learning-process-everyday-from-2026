#score calculator

score = int(input("Enter your exam score (0-100): "))

if score > 100:
    print("invalid score ")

elif score >= 90:
    print("You got an A!")

elif score >= 50:
    print("You passed!")

else:
    print("You failed.")
