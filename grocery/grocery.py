"""
Problem:
Keep taking grocery items from the user until they press Ctrl+D. Then print each item with how many times it was entered, in alphabetical
order and in uppercase. Example: "2 APPLE".

Approach:
I used a dictionary to store the items and their count. In a while loop I take the input in lowercase. If the item is already in the dictionary I add 1 to its count, 
else I set it to 1. Ctrl+D gives an EOFError, so I catch it and break the loop. At the end I loop through the sorted items and print the count and the item in uppercase.
"""

grocery = {}

while True:
    try:
        i = input().lower()

        if i in grocery:
            grocery[i] += 1
        else:
            grocery[i] = 1

    except EOFError:
        break

for i in sorted(grocery):
    print(grocery[i], i.upper())
