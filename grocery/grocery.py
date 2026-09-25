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
