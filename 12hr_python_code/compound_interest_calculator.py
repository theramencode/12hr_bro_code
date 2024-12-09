print("Hello! This is the Compound Interest Calculator, I hope you enjoy!")

principal = float(input("Enter your starting value ($): "))

while principal <= 0:
    print("Your starting value input is invalid")
    principal = float(input("Enter your starting value ($): "))
term = float(input("Time (in years) compounded: "))

while term <= 0:
    print("Your time input is invalid")
    term = float(input("Time (in years) compounded: "))
rate = float(input("Enter the rate (in %) at which your money is compounding at: "))

while rate <= 0:
    print("Your interest rate input is invalid")
    rate = float(input("Enter the rate at which your money is compounding at (months): "))
rate /= 100
contribution_check = str(input("Are you contributing monthly (Y/N)?: "))

while contribution_check == "":
    print("Your contribution input is invalid")
    contribution_check = str(input("Are you contributing monthly (Y/N)?: "))

if contribution_check == "Y":
    contribution_amount = float(input("Enter what are you contributing monthly ($): "))
    result = principal * pow( 1 + (rate / 12), 12 * term) + contribution_amount * (pow(1 + (rate / 12), 12 * term) - 1) / (rate / 12)
    print(f"After {term} years of compound interest and ${contribution_amount} contributed monthly, you would be left with a total of ${round(result,2):,}")

elif contribution_check == "N":
    result = principal * pow((1 + rate), term)
    print(f"After {term} years of compound interest, you would be left with a total of ${round(result,2):,}")

else:
    print("Your contribution input was invalid")
    contribution_check = str(input("Are you contributing monthly (Y/N)?: "))