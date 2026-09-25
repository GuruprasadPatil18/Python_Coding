math = input("Expression: ")
x, y, z = math.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x+z))
if y == "-":
    print(float(x-z))
if y == "*":
    print(float(x*z))
if y == "/":
    if z != 0:
        print(float(x/z))


