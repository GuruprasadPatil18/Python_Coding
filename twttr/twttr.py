wv = input("Input: ")

output = ""

for i in wv:
    if i.lower() not in "aeiou":
        output += i

print("Output:", output)
