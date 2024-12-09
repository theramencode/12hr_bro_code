# Basic Math Applications and Simplify

friends = 10
remainder = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2
# remainder %= 2

print (remainder)

# Math Functions

x = 3.14
y = -4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4,3)
# result = max(x, y , z)
result = min(x, y, z)

print(result)

# Constants and Functions

import math

x = 9.1

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
result = math.floor(x)

print(result)

# Exercise 1 Circumference of A Circle

import math

radius = float(input("Enter the radius of your circle: "))
circumference = 2 * math.pi*radius

print(f"The circumference of your circle is {round(circumference, 2)} units²")

# Exercise 2 Area of A Circle

import math

radius = float(input("Enter the radius of your circle: "))
area = math.pi * pow(radius, 2)

print(f"The area of your circle is {round(area, 2)} units²")

# Exercise 3 Hypotenuse of a Right Triangle

a = float(input("Enter the first side length of your right triangle: "))
b = float(input("Enter the second side length of your right triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Hypotenuse of the right triangle is {round(c,2)} units²")