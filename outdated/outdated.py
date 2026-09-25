months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if month < 1 or month > 12 or day < 1 or day > 31:
                continue

        else:
            month, day, year = date.split(" ")

            if month not in months:
                continue

            if not day.endswith(","):
                continue

            day = int(day.replace(",", ""))

            if day < 1 or day > 31:
                continue

            month = months.index(month) + 1
            year = int(year)

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        pass
