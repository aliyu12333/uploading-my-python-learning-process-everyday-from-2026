 # Logical operators = are used on conditional statements

 #               and = checks if two or more conditions are true
 #                or = checks if at least one condition is true
 #               not = check  condition is false, vice versa

temp = 0
sunny = False
if temp > 0 and temp <  30:
     print("the temperature is good")

if temp <= 0 or temp >= 30:
    print("the temperature is bad")

if not sunny:
     print("it is sunny")

else:
    print("it is cloudy outside")