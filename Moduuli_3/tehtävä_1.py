while True:
    try:
        int1 = float(input("Syötä kuhan pituus senttimetreinä: \n"))
        if int1 < 37:
            print("Kuhan pituus ei ole tarpeeksi pitkä, laskethan sen takaisin järveen kasvamaan")
            print("Kuha pitäisi olla vähintään 37cm pitkä")
        else:
            break
    except ValueError as err:
        print(f"Error -> {err.args}!!!")
