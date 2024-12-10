# format specifiers = {:flags} format a value base on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :  = place sign to leftmost position
# :, = comma separator

price1 = 30002130.14159
price2 = -987032032.65
price3 = 12123131.34

print(f"Price 1 is ${price1:+,.3f}")
print(f"Price 2 is ${price2:+,.3f}")
print(f"Price 3 is ${price3:+,.3f}")