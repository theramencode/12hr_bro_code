unit_of_measurement = input("Enter your current unit of measurement (kg/lbs): ")
weight = float(input("Enter your weight: "))

if unit_of_measurement == "kg":
    lb = weight * 2.20462
    print(f"Your weight is {round(lb, 2)} pounds")
elif unit_of_measurement == "lbs":
    kg = weight * 0.453592
    print(f"Your weight is {round(kg, 2)} kilograms")
else:
    print("Your unit of measurement is invalid")

