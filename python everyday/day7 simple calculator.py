#simple python calculator

operator = input("enter an operator: ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "+":
    result1 = num1 + num2
    print(result1)

elif operator == "-":
    result2 = num1 - num2
    print(result2)

elif operator == "*":
    result3 = num1 * num2
    print(result3)

elif operator == "/":
    result4 = num1 / num2
    print(result4)

else:
    print("invalid inputs")
