class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumäärä)


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Päätoimittaja:", self.päätoimittaja)


aku = Lehti("Aku Ankka", "Aki Hyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
aku.tulosta_tiedot()
print("--------------------")
hytti.tulosta_tiedot()
