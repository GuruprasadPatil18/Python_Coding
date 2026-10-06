"""
Problem:
Print the list of all the fonts available in the pyfiglet package.

Approach:
I used the pyfiglet package, which is installed with pip. I imported Figlet and made a Figlet object. Then I used its getFonts() method to
get the list of fonts and printed it.
"""

from pyfiglet import Figlet

figlet = Figlet()

print(figlet.getFonts())
