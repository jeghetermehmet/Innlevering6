from motorsykkel import Motorsykkel

def hovedprogram():
    Honda = Motorsykkel("Honda", "XC233")
    Kawazaki = Motorsykkel("Kawazaki", "ER145")
    Elsykkel = Motorsykkel("Elsykkel", "TY456")
    Honda.skriv_ut()
    Kawazaki.skriv_ut()
    Elsykkel.skriv_ut()
    Elsykkel.kjor(10)
    assert Elsykkel.hent_kilometeravstand() == 10
    print(Elsykkel.hent_kilometeravstand())


hovedprogram()
