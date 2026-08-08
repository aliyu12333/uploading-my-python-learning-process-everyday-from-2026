# email slicer
import sys
email = input("ENTER YOUR EMAIL: ")

if " " in email:
    print("there cannot be space in your email address")
    sys.exit()

elif not "@" in email:
    print("there must be @ in you email address")
    sys.exit()
index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"your username is {username} and the domain name is {domain}")

#partially AUthored by aliyu