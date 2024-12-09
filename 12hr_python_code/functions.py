# function = A block of reusable code
#            place () after the function name to invoke it

def birthday_song(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to you!")
    print() 

birthday_song("Naman", 14)
birthday_song("Steve", 20)
birthday_song("Joe", 30)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Naman", 21312312.52, "5/23")

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("naman", "rohit")

print(full_name)