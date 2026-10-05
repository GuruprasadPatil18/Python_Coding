"""
Problem:
Keep taking names from the user until they press Ctrl+D. Then print "Adieu, adieu, to" followed by all the names. For two names use "and" between them. For three or more, use commas and put "and" before the last name.

Approach:
I used a while loop to take the names and store them in a list. When Ctrl+D is pressed it gives an EOFError, so I handle it with try/except and break the loop. After that I check how many names are in the list and join them in the right format. Then I print the final message.
"""
names = []

while True:
    try:
        print("Name: ",end="")
        name = input()
        names.append(name)
        print(names)
    except EOFError:
        print()
        break

if len(names) == 1:
    result = names[0]

elif len(names) == 2:
    result = " and ".join(names)

else:
    result = ", ".join(names[:-1]) + ", and " + names[-1]

print("Adieu, adieu, to " + result)
