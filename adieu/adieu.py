# Taking multiple names as input and put them into a farewell msg
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
