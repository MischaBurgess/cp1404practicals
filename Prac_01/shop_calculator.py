no_of_items = int(input("Number of items?: "))

while no_of_items <= 0:
    print("Invalid number of items!")
    no_of_items = int(input("Number of items?: "))
for i in range(0, no_of_items):
    item_prices = float(input(("Price of item?: ")))
    total = item_prices + item_prices
    if total > 100:
        total = (total * 0.9)
print("Your total for {} items"" is: ${}".format(no_of_items, round(total, 2)))
