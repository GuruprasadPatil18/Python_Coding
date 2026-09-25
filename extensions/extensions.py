ex = input("File name: ")

ex = ex.lower().strip()

for i in [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]:

    if ex.endswith(i):
        if i == ".gif":
            print("image/gif")
        elif i == ".jpg" or i == ".jpeg":
            print("image/jpeg")
        elif i == ".png":
            print("image/png")
        elif i == ".pdf":
            print("application/pdf")
        elif i == ".txt":
            print("text/plain")
        elif i == ".zip":
            print("application/zip")
        break

else:
    print("application/octet-stream")
