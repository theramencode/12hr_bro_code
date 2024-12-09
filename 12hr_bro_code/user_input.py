# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you: "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("What is the length of the rectangle?: "))
width = float(input("What is the width of the rectangle: "))
area = length*width

print(f"The area of the rectangle is: {area} units²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like to buy: "))
total = price*quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total cost is: ${total}")