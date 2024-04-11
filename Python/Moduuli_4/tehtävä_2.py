while True:
    try:
        value = int(input("Syötä tuumat \n"))
        if value < 0:
            print("Syötit negatiivisen tuumamäärän, ohjelma itsetuhoutuu 💣💣💣")
            break

        cm = value * 2.54
        print("Syöttämäsi tuumat senttimetreinä: " + str(cm))


    except:
        print("Syötä vain kokonaisluvut!")