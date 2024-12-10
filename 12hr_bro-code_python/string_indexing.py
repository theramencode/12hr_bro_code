# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-5])
# print(credit_number[::4])

last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

credit_number = credit_number[::-1]
print(credit_number)