Temperature = float(input("Enter the current temperature?: "))
Unit = input("Enter current unit (Fahrenheit/Celsius): ")

if Unit == "Fahrenheit":
    result = (Temperature - 32) * 5/9
    Unit = "Celsius"
    print(f"The temperature is {round(result, 3)} degrees {Unit}")
elif Unit == "Celsius":
    result = ( 9/5 * Temperature) + 32
    Unit = "Fahrenheit"
    print(f"The temperature is {round(result, 3)} degrees {Unit}")
else:
    print("Your inputs are invalid.")