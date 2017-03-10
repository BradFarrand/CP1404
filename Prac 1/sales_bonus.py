"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

while True:
    sales = float(input("Enter sales: $"))
    if sales > 0 and sales < 1000:
        bonus_rate = 1.1
    elif sales >= 1000:
        bonus_rate = 1.15
    else:
        break

    total_sale = sales * bonus_rate
    bonus_sale = total_sale - sales
    print("The bonus on your sale is $" + str(bonus_sale))
