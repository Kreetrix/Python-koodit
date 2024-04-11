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


h = Hissi()
h.siirry_kerrokseen(7)
h.siirry_kerrokseen(2)
