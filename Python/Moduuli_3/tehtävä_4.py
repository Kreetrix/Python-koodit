while True:
    try:
        year = int(input("Syötä vuosiluku: \n"))

        if year % 4 == 0 or (year % 100 == 0 and year % 4 == 0):
            print("Vuosi on karkausvuosi!")
        else:
            print("Vuosi ei ole karkausvuosi!")

    except ValueError as err:
        print(f"Error -> {err.args}")
