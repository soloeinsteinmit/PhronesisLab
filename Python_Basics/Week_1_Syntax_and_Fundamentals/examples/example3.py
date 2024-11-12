# Declaring and manipulating variables
import time


print("taking inputs from user")
num1 = input("Enter number1: ")
num2 = input("Enter number2: ")

time.sleep(2)
print("checking for type...")
time.sleep(2)
# checking type before conversion
print(f'type of num1 before conversion -> {type(num1)}')
print(f'type of num2 before conversion -> {type(num2)}\n')

time.sleep(2)
print("converting to int...")
time.sleep(2)
# convert to int
num1 = int(num1)
num2 = int(num2)

time.sleep(2)
print("checking for type after conversion")
time.sleep(2)
# check type after conversion
print(f'type of num1 after conversion -> {type(num1)}')
print(f'type of num2 after conversion -> {type(num2)}\n')

time.sleep(2)
print("calculating the result...")
time.sleep(2)
result = num1 + num2
print(f"result for num1 & num2 is -> {result}")

# age = 12
# string, integer, double, boolean
name = "Alice" # string
#
dob = "2004"
years = "2024"
#
isOld = True

# checking data type
print(type(dob))
print(type(789))
print(type(isOld))
print(type(900.99))

age = years + dob

print(age)

# string concatenation
# methods
print("method1")
print( name + " is " + years + " years of age" )
#      Alice    is     2003      years of age

# methods 2
print("\nmethod2\n")
print(name, " is ", years, " years of age")

# string interpolation/ formatted strings
print("\nmethod3")
print(f"\t{name} is {years} years of age")

# escape sequences
# \t -> tab
# \n -> new line
# \r -> carriage return
# \b -> backspace
# \' -> single quote
# \" -> double quote
# \\ -> backslash

