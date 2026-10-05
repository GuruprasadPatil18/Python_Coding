"""
Problem:
Take a text input from the user and replace ":)" with 🙂 and ":(" with 🙁. The rest of the text stays the same.

Approach:
I made a convert() function that uses replace() to change ":)" and ":(" to the emojis and returns the new text. In main() I take the input, send it to convert() and print the result.
"""

def convert(a):
    a = a.replace(":)","🙂")
    a = a.replace(":(","🙁")
    return a
def main():
    ip = input()
    b = convert(ip)
    print(b)

if __name__ =="__main__":
    main()


