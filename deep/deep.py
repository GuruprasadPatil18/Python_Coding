"""
Problem:
Ask the user for the answer to the Great Question of Life, the Universe, and Everything. If the answer is 42, forty-two or forty two, print "Yes".
Otherwise print "No".

Approach:
I took the input and used lower() and strip() so capital letters and extra spaces don't matter. Then I used if and elif to compare it with "42", "forty-two" and "forty two". 
If any of them match I print "Yes", else I print "No".
"""
a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
a = a.lower().strip()
if a == "42":
    print("Yes")
elif a == "forty-two":
    print("Yes")
elif a == "forty two":
    print("Yes")
else:
    print("No")

