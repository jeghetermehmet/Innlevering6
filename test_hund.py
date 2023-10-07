from hund import Hund

def hovedprogram():
    bambi = Hund(2, 6)
    bambi.spring()
    print("Bambis vekt er", bambi.hent_vekt())
    bambi.spis(1)
    print("Bambis vekt er", bambi.hent_vekt())
    bambi.spring()
    print("Bambis vekt er", bambi.hent_vekt())
    bambi.spis(2)
    print("Bambis vekt er", bambi.hent_vekt())
hovedprogram()



    