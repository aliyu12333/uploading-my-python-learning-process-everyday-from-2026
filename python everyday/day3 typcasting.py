#typecasting = the act of changing one data type to another eg from float to integer or from boolean to variale and so on and so on
#             implicit vs explicit type casting

#implicit typecasting

age = 16
gpa = 4.5
name = "aliyu"
student = True

print(type(age))
age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

age = bool(age)
print(type(age))
print(age)

#explicit typecasting

x = 2
y = 1.0
z = x + y
print(z)