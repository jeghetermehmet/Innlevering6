from dato import Dato
def hovedprogram():
    date = Dato(1, 3, 23)
    print("Nå er vi i", date.hent_aar(), "året")
    if date.hent_ny_dag() == 15:
        print("Loenningsdag!")
    elif date.hent_ny_dag() == 1:
        print("Ny maaned, nye muligheter")
    print(date.tekststreng())


    