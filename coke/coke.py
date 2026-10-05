"""
Problem:
A coke costs 50 cents. Keep asking the user to insert coins until the full amount is paid. Only 25, 10 and 5 are accepted, other coins are ignored. 
At the end print the change owed.

Approach:
I started with the amount due as 50 and used a while loop that runs till it is 0 or less. Each time I print the amount due and take a coin.
If the coin is 25, 10 or 5, I subtract it from the amount due. After the loop, the amount due is 0 or negative, 
so I use abs() to print the change.
"""

ad = 50

while ad>0:
    print("Amount Due:", ad)

    ic = int(input("Insert Coin: "))

    if ic == 25 or ic == 10 or ic == 5:
        ad = ad - ic
print("Change Owed:", abs(ad))

