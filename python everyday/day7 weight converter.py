#simple python weight converter

weight = float(input("enter your weight: "))
unit = input("enter your weight unit kilograms or pound: (K or L)'")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is {round(weight, 2)} in {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"your weight is {round(weight, 2)} in {unit}")

else:
    print(f"{unit} is invalid unit")


