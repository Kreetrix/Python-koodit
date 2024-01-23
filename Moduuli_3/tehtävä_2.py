while True:
    try:
        value = str(input("Syötä laivan hyttiluokka: \n")).capitalize()
        if value == "LUX":
            print("LUX on parvekkeellinen hytti yläkannella.")
        elif value == "A":
            print("A on ikkunallinen hytti autokannen yläpuolella.")
        elif value == "B":
            print("B on ikkunaton hytti autokannen yläpuolella.")
        elif value == "C":
            print("C on ikkunaton hytti autokannen alapuolella.")
        else:
            print("Virheellinen hyttiluokka")

    except ValueError as err:
        print(f"Error -> {err.args}")
