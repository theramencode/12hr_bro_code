# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 70
is_raining = False

if temp > 90 or temp < 32 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

temp = 16
is_sunny = True

if temp >= 90 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 32 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 90 > temp > 32 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 90 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 32 and not is_sunny:
    print("It is COLD outside")
    print("It is COLD")
elif 90 > temp > 32 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")