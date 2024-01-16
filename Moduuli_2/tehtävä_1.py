placeholder = False


def print_nimi() -> bool:
    nimi = input("Syötä nimisi: \n")
    if nimi.isalpha():
        print("Moi, " + nimi)
        return True
    else:
        print("Syötä vain kirjaimet!")
        return False


while not placeholder:
    print_nimi()
