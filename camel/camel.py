cs = input("camelCase: ")

snake = ""

for i in cs:
    if i.isupper():
        snake += "_" + i.lower()
    else:
        snake += i

print("snake_case:",snake)
