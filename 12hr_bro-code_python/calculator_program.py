operator = input("Enter the operator you want to use (+, -, *, /): ")
num_1 = float(input("Enter the 1st number: "))
num_2 = float(input("Enter the 2nd number: "))

if operator == "+":
    answer = num_1 + num_2
    round(answer,3)
    print(f"Your answer is: {answer}")
elif operator == "-":
    answer = num_1 - num_2
    round(answer, 3)
    print(f"Your answer is: {answer}")
elif operator == "*":
    answer = num_1 * num_2
    round(answer, 3)
    print(f"Your answer is: {answer}")
elif operator == "/":
    answer = num_1 / num_2
    round(answer, 3)
    print(f"Your answer is: {answer}")
else:
    print("The operator you typed in was invalid")