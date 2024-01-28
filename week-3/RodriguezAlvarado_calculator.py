"""
    Title: RodriguezAlvarado_calculator.py
    Author: Zadkiel Rodriguez Alvarado
    Date: 01/28/2024
    Description: Calculator in python
    Sources: https://docs.python.org/3/tutorial/inputoutput.html 
"""
# Functions
# add function
def add(num1, num2):
    return num1 + num2

# subtract function
def subtract(num1, num2):
    return num1 - num2

# divide function
def divide(num1, num2):
    return num1 / num2

# multiply function
def multiply(num1, num2):
    return num1 * num2

# Variables
# add variables
num1_add = 4
num2_add = 4

# subtract variables
num1_subtract = 10
num2_subtract = 6

# divide variables
num1_divide = 8
num2_divide = 2

# multiply variables
num1_multiply = 10
num2_multiply = 2

# Build result string
results = ""
results += f"{num1_add} + {num2_add} is {add(num1_add, num2_add)}.\n"
results += f"{num1_subtract} - {num2_subtract} is {subtract(num1_subtract, num2_subtract)}.\n"
results += f"{num1_divide} / {num2_divide} is {divide(num1_divide, num2_divide)}.\n"
results += f"{num1_multiply} * {num2_multiply} is {multiply(num1_multiply, num2_multiply)}.\n"

# Print result string
print(results)