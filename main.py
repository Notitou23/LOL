class Instrument:
    def __init__(self, son, taille, tipe, color):
        self._son = son
        self._taille = taille
        self._type = tipe
        self._color = color

    def info(self):
        print("Son:", self._son, "\nTaille:", self._taille, "\nType:", self._type, "\nCouleur", self._color)

    def broken(self):
        print("Oups l'instrument ne fonctionne plus")


class Ocarina(Instrument):
    def __init__(self, son, taille, tipe, color, cool):
        super().__init__(son, taille, tipe, color)
        self._cool = cool

    def broken(self):
        print("Impossible l'ocarina ne peut pas se casser")

    def jouer(self):
        print("juuuuuuuulk")


class Cuillere(Instrument):
    def __init__(self, son, taille, tipe, color, bruyant):
        super().__init__(son, taille, tipe, color)
        self._bruyant = bruyant

    def info(self):
        print("Son:", self._son, "\nTaille:", self._taille, "\nType:", self._type, "\nCouleur", self._color,
              "\nBruyant:", self._bruyant)

    def manger(self):
        print("NON tu n'es pas supposé faire ça")


ocarina = Ocarina("Melodieux", 20, "Vent", "Bleu", "YES")
cuillere = Cuillere("Brusque", 15, "Percussion", "Gris", "Oui")
ocarina.broken()
ocarina.info()
ocarina.jouer()
cuillere.broken()
cuillere.info()
cuillere.manger()
