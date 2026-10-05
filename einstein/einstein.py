"""
Problem:
Ask the user for mass in kilograms and print the energy in joules using Einstein's formula E = mc^2.

Approach:
I stored c squared in a variable, using 300000000 as the speed of light.
Then I took the mass as an integer input and multiplied it with c squared. At the end I print the result.
"""

c = 300000000 * 300000000
m = int(input("m: "))
print("E: ",m*c)
