# for loops = execute a block of code a fix number of times.
#             You can iterate over a range, string, sequence, etc.

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)

for x in reversed(range(1, 11, 2)):
    print(x)
print("HAPPY NEW YEAR!")