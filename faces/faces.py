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


