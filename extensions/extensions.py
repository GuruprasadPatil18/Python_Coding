"""
Problem:
Ask the user for a file name and print its media type based on the extension. 
Supported ones are gif, jpg, jpeg, png, pdf, txt and zip. If it is anything else, print application/octet-stream.

Approach:
I took the input and used lower() and strip() so capital letters and spaces don't matter. Then I looped through the list of extensions and
checked each one with endswith(). If it matches, I print the media type and break. If nothing matches, the else part of the loop prints
application/octet-stream.
"""

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
