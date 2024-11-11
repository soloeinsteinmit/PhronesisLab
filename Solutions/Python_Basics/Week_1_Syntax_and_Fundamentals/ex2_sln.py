# Tip Calculator

# Ask the user to enter the total bill amount
bill_amount = float(input("Enter the total bill amount: "))

# Ask the user to choose a tip percentage
print("Choose a tip percentage:")
print("1. 10%")
print("2. 15%")
print("3. 20%")

# Get the user's choice
tip_option = int(input("Enter your choice (1-3): "))

if tip_option == 1:
    tip_percentage = 0.10
elif tip_option == 2:
    tip_percentage = 0.15
elif tip_option == 3:
    tip_percentage = 0.20
else:
    print("Invalid choice. Using 15% tip.")
    tip_percentage = 0.15

# Calculate the tip amount and total bill
tip_amount = bill_amount * tip_percentage
total_bill = bill_amount + tip_amount

# Print the results
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total bill: ${total_bill:.2f}")