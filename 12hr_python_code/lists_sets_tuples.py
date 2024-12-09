# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "orange", "banana"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apples" in fruits)

# fruits[0] = "grape"
# fruits.append("kiwi")
# fruits.remove("banana")
# fruits.insert(0, "apple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
print(fruits.count("banana"))

# print(fruits[0:4:2])
# for fruit in fruits:
#    print(fruits)

fruits = {"apple", "orange", "banana", "coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apples" in fruits)

fruits.add("pineapple")

# NO print(fruits[0:4:2])

fruits = ("apple", "orange", "banana", "coconut")

print(fruits)

for fruit in fruits:
    print(fruit)

