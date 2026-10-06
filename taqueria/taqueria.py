"""
Problem:
Keep asking the user for items from a taqueria menu until they press Ctrl+D. After each item, print the total so far with a $ sign and 2 decimal places. 
If the item is not on the menu, ignore it.

Approach:
I made a dictionary with the item names and their prices. In a while loop I take the input and use title() so capital letters don't matter.
If the item is in the menu, I add its price to the total and print it. Ctrl+D gives an EOFError, so I catch it and break the loop.
"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        i = input("Item: ").title()

        if i in menu:
            total += menu[i]
            print(f"Total: ${total:.2f}")

    except EOFError:
        print()
        break
