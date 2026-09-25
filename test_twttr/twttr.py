def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    output = ""

    for i in word:
        if i.lower() not in "aeiou":
            output += i

    return output


if __name__ == "__main__":
    main()
