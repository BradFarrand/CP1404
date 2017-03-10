count_items = 0
number_of_items = int(input("Please enter the number of items"))
while number_of_items <0:
    number_of_items = int(input("Invalid number of items. Please enter the number of items"))
prices_of_items = []
while number_of_items > count_items:
    price_of_item = float(input("Please enter the price of each item"))
    count_items = count_items + 1
    prices_of_items.append(price_of_item)
print("You have purchased", number_of_items, "items.")
for price in (prices_of_items):
    print("Your item cost $" + str(price))
total = sum(prices_of_items)
if total > 100:
    total = total * 0.9

print("Your total price for", number_of_items, "items is $" + str(total))
