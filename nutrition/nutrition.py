"""
Problem:
Ask the user for a fruit name and print its calories. If the fruit is not in the list, print nothing.

Approach:
I made a dictionary with the fruit names and their calories. I took the input and used lower() so capital letters don't matter. 
If the fruit is in the dictionary, I print its calories.
"""

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

i = input("Item: ").lower()

if i in fruits:
    print("Calories:", fruits[i])
