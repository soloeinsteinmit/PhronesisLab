# Temperature Converter

# Ask the user to enter the temperature in Celsius
celsius_temp = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temp = (celsius_temp * 9/5) + 32

# Print the conversion
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F.")