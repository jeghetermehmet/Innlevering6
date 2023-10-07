class Motorsykkel:
    def __init__(self, merke, regnummer):
        self._kmavstand = 0
        self._merke = merke
        self._regnummer = regnummer
    def kjor(self, km):
        self._kmavstand += km
    def hent_kilometeravstand(self):
        return self._kmavstand
    def skriv_ut(self):
        print("Merke:", self._merke, "Registeringsnummer:", self._regnummer, "har kjørt", self._kmavstand)