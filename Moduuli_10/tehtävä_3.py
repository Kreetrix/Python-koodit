
class Hissi:
    def __init__(self):
        self.alin_kerros = 0
        self.ylin_kerros = 10
        self.kerros = 0

    def kerros_ylös(self):
        self.kerros += 1
        print(f'{self.kerros} ylös')

    def kerros_alas(self):
        self.kerros -= 1
        print(f'{self.kerros} alas')

    def siirry_kerrokseen(self, kerros):
        if self.alin_kerros <= kerros <= self.ylin_kerros:
            if self.kerros <= kerros:
                while self.kerros != kerros:
                    self.kerros_ylös()
            if self.kerros >= kerros:
                while self.kerros != kerros:
                    self.kerros_alas()

class Talo:
    def __init__(self):
        self.hissit = [Hissi() for i in range(0, 4)]
        self.alin_kerros = 0
        self.ylin_kerros = 10

    def aja_hissiä(self, hissi_id, kerros):
        self.hissit[hissi_id].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.alin_kerros)

t = Talo()
t.aja_hissiä(1, 10)
t.palohälytys()
