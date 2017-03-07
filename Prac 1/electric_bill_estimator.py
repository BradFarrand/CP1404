TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

get_tariff = int(input("Please enter which tariff you\'re using: 11 or 31"))
if get_tariff != 11 or get_tariff != 31:
    get_tariff = int(input("Invalid tariff. Please enter which tariff you\'re using: 11 or 31"))
get_daily_usage = float(input("Please enter daily use in kWh"))
get_days = int(input("Please enter number of days in the billing period."))
if get_tariff == 11:
    bill_estimate = float(TARIFF_11 * get_daily_usage * get_days)
else:
    bill_estimate = float(TARIFF_31 * get_daily_usage * get_days)
print("Your estimated bill equals $", bill_estimate)
