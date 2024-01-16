while True:
    try:
        suorakulmion_kanta = float(input("Syötä suorakulmion kanta: \n"))
        suorakulmion_korkeus = float(input("Syötä suorakulmion korkeus: \n"))
        suorakulmion_piiri = suorakulmion_kanta * 2 + suorakulmion_korkeus * 2
        suorakulmion_pinta_ala = suorakulmion_kanta * suorakulmion_korkeus
        print("Suorakulmion piiri: " + str(suorakulmion_piiri) + "\n")
        print("Suorakulmion pinta-ala: " + str(suorakulmion_pinta_ala) + "\n")
        break
    except:
        print("Käytä vain reaalilukuja!!!")