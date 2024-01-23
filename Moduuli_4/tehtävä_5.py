valid_login = "python"
valid_password = "rules"
attempts = 0

while True:
    input_login = str(input("Syötä käyttäjätunnus: "))
    input_password = str(input("Syötä salasana: "))
    if input_login == valid_login and input_password == valid_password:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana!")
        attempts += 1
        if attempts >= 5:
            print("Pääsy evätty!")
            break