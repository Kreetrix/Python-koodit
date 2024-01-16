import math

while True:
    try:
        säde = float(input("Syötä ympyrän säde: \n"))
        pinta_ala = säde ** 2 * math.pi
        print("ympyrän pinta ala: " + str(pinta_ala))
        break
    except:
        print("Käytä vain reaalilukuja!!!")