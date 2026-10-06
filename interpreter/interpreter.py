"""
Problem:
Ask the user for a math expression like "2 + 3". Do the calculation for +, -, * or / and print the answer as a float.

Approach:
I took the input and split it into the first number, the symbol and thevsecond number. I changed both numbers to int. Then I used if statements
to check the symbol and print the answer as a float. For division I check that the second number is not 0 first.
"""

math = input("Expression: ")
x, y, z = math.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x+z))
if y == "-":
    print(float(x-z))
if y == "*":
    print(float(x*z))
if y == "/":
    if z != 0:
        print(float(x/z))


