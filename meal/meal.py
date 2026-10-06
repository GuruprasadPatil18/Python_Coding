"""
Problem:
Ask the user for the time like "7:30" and print the meal time if it falls in any one. Breakfast is 7 to 8, lunch is 12 to 13 and dinner is 18 to 19. 
If it is none of these, print nothing.

Approach:
I made a convert() function that splits the time at ":" and changes it into hours. The minutes are divided by 60 and added to the hours, 
so 7:30 becomes 7.5. In main() I take the input, send it to convert() and use if and elif to check which meal time it is.
"""

def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
