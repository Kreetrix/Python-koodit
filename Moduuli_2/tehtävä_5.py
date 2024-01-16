import math

while True:
    try:
        leviskät = float(input("Syötä leviskät: \n")) * 20
        naulat = float(input("Syötä naulat: \n")) * 32
        luodit = float(input("Syötä luodit: \n"))
        grams = (leviskät * 32 + naulat + luodit) * 13.3
        kilos, grams = divmod(grams, 1000)
        print("Massa nykymittojen mukaan: \n")
        print(str(kilos) + " kilogrammaa")
        print(str(math.trunc(grams)) + " grammaa")
        break
    except:
        print("Käytä vain reaalilukuja!!!")
