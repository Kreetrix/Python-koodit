while True:
    try:
        int1 = float(input("Syötä kuhan pituus senttimetreinä: \n"))
        if int1 < 37:
            print("Kuhan pituss ei ole tarpeeksi pitkä, laskethan sen takaisin järveen kasvamaan")
            print("Kuha pitäisi olla vähintään 37cm pitkä")
        else:
            break
    except:
        print("Syötä vain reaalilukuja!!!")
