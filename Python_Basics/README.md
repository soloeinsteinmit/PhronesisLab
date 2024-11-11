# Week 1 - Python Basics: Syntax and Fundamentals

## 🌟 Overview

Welcome to the first week of our Python Basics journey! In this module, we'll dive into the fundamental building blocks of Python programming. You'll learn about Python's syntax, data types, variables, and basic operations - laying a solid foundation for your coding adventures.

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Set up your Python development environment.
2. Understand and use Python's basic syntax.
3. Declare and work with different data types, including integers, floats, strings, and booleans.
4. Create and manipulate variables.
5. Perform basic arithmetic and logical operations.
6. Write simple Python programs that utilize the concepts covered.

## 📚 Lessons

### Lesson 1: Python Setup and Environment

- Installing Python on your operating system
- Choosing a code editor (e.g., VS Code, Jupyter Notebook)
- Running Python code in the terminal or an IDE

### Lesson 2: Python Syntax and Data Types

- Printing output with `print()`
- Inputing data with `input()`
- Using comments to document your code (single-line and multi-line comments)
- Understanding integers, floats, strings, and booleans
- Declaring and assigning values to variables
  - Example:
  ```python
  name = "Alice"
  age = 25
  is_student = True
  ```

### Lesson 3: Operators and Expressions

- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
  - Example:
  ```python
  x = 10
  y = 5
  addition = x + y
  ```
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- Combining operators to form expressions
  - Example:
  ```python
  x = 10
  y = 5
  z = 15
  print("x > y and x < z:", x > y and x < z)  # True
  ```

## 💻 Examples

### Example 1: Simple Arithmetic Operations

```python
# Performing basic arithmetic
x = 10
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponent = x ** 2
floor_division = x // y

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponent:", exponent)
print("Floor Division:", floor_division)
```

### Example 2: Input and Output

```python
# Demonstrating input and output
name = input("Enter your name: ")
print("Hello,", name)

# Prompting user input
x_input = int(input("Enter the first number: "))
y_input = int(input("Enter the second number: "))

result = x_input + y_input
print("The sum of", x_input, "and", y_input, "is", result)
```

### Example 3: Working with Variables and Data Types

```python
# Declaring and manipulating variables
name = "Alice"
age = 25
is_student = True

print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)

# Converting data types
age_as_string = str(age)
print("Age as String:", age_as_string)

student_as_int = int(is_student)
print("Student as Integer:", student_as_int)
```

### Example 4: Using Logical Operators

```python
# Demonstrating logical operators
x = 10
y = 5
z = 15

# Logical AND
print("x > y and x < z:", x > y and x < z)  # True

# Logical OR
print("x > y or x > z:", x > y or x > z)  # True

# Logical NOT
print("not is_student:", not is_student)  # False
```

## 🤔 Exercises

### Exercise 1: Currency Converter

Write a program that converts US dollars to Euros. The program should:

1. Prompt the user to enter an amount in US dollars.
2. Convert the amount to Euros using an exchange rate of 1 USD = 0.85 EUR. Or use any other exchange rate you prefer.
3. Print the converted amount in Euros(or your converted currency).

### Exercise 2: Tip Calculator

Develop a program that calculates the tip for a restaurant bill. The program should:

1. Prompt the user to enter the total bill amount.
2. Allow the user to choose a tip percentage (10%, 15%, or 20%).
3. Calculate the tip amount and the total bill (including the tip).
4. Print the tip amount and the total bill.

### Exercise 3: Area of a Circle

Create a program that calculates the area of a circle. The program should:

1. Prompt the user to enter the radius of the circle.
2. Calculate the area using the formula: `area = π * radius^2`.
3. Print the calculated area.

### Exercise 4: Odd or Even

Write a program that determines whether a number is odd or even. The program should:

1. Prompt the user to enter a whole number.
2. Determine if the number is odd or even using the modulo operator.
3. Print whether the number is odd or even.

### Exercise 5: Age Calculator

Develop a program that calculates a person's age. The program should:

1. Prompt the user to enter their birth year.
2. Calculate the person's age based on the current year (assume the current year is 2023).
3. Print the person's age.

### Exercise 6: Temperature Converter

Create a program that converts temperature from Celsius to Fahrenheit. The program should:

1. Prompt the user to enter a temperature in Celsius.
2. Convert the temperature to Fahrenheit using the formula: `F = (C * 9/5) + 32`.
3. Print the converted temperature in Fahrenheit.

## 🔍 Solutions

Solutions to the exercises are provided in the `Solutions` folder.

## 📝 Reflection

Great work 🥳 completing the first week of Python Basics! You've learned the fundamentals of Python syntax, data types, and basic operations. These concepts form the foundation for more advanced programming techniques and problem-solving.

As you move forward, keep the following in mind:

- Practice the concepts covered in this week's lessons by experimenting with the examples and exercises.
- Challenge yourself by modifying the existing code or coming up with your own creative solutions.
- Refer to the well-documented examples and solutions when you need guidance or want to compare your work.
- Ask questions, seek clarification, and explore deeper topics that pique your interest.

Remember, becoming a proficient programmer is a journey. Keep up the momentum, and you'll be writing robust, meaningful code in no time!
