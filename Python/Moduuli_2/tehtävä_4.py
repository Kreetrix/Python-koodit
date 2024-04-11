while True:
    try:
        int1 = int(input("Syötä ensimmäinen kokonaisluku: \n"))
        int2 = int(input("Syötä toinen kokonaisluku: \n"))
        int3 = int(input("Syötä kolmas kokonaisluku: \n"))
        print("Summa: " + str(int1 + int2 + int3) + "\n")
        print("Tulo: " + str(int1 * int2 * int3) + "\n")
        print("Keskiarvo: " + str((int1 + int2 + int3) / 3) + "\n")
        break
    except:
        print("Käytä vain integraaleja!!!")
