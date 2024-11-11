# Currency Converter

# Ask the user to enter an amount in US dollars
usd_amount = float(input("Enter an amount in US dollars: "))

# calculate eur amount
eur_amount = usd_amount * 0.85

# print conversion
print(f"{usd_amount} USD is equal to {eur_amount:.2f} EUR")