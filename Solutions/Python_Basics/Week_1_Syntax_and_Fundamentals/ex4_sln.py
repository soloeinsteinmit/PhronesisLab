# Odd or Even

# Ask the user to enter a whole number
number = int(input("Enter a whole number: "))

# Determine if the number is odd or even
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")