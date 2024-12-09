
name = input("Enter your full name: ")
phone_number = (input("Enter your phone number: "))

# result = len(name)
# result = name.find("a")
# result = name.rfind("z")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
phone_number = phone_number.replace("-","")

print(phone_number)

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

Username = input("Enter your username: ")

if len(Username) > 12:
    print("Your username is longer than 12 characters.")
elif not Username.find(" ") == -1:
    print("Your username contains spaces.")
elif not Username.isalpha():
    print("Your username contains digits.")
else:
    print("Your username has been configured properly.")