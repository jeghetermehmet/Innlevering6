class Dato:
    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self._ny_dag = ny_dag
        self._ny_maaned = ny_maaned
        self._nytt_aar = nytt_aar
    def hent_aar(self):
        return self._nytt_aar
    def hent_ny_dag(self):
        return self._ny_dag
    def tekststreng(self):
        self._ny_dag = str(self._ny_dag)
        self._nytt_aar = "20" + str(self._nytt_aar)
        if self._ny_maaned == 1:
            self._ny_maaned = str("januar")
        elif self._ny_maaned == 2:
            self._ny_maaned = str("februar")
        elif self._ny_maaned == 3:
            self._ny_maaned = str("march")
        elif self._ny_maaned == 4:
            self._ny_maaned = str("april")
        elif self._ny_maaned == 5:
            self._ny_maaned = str("may")
        elif self._ny_maaned == 6:
            self._ny_maaned = str("june")
        elif self._ny_maaned == 7:
            self._ny_maaned = str("july")
        elif self._ny_maaned == 8:
            self._ny_maaned = str("august")
        elif self._ny_maaned == 9:
            self._ny_maaned = str("september")
        elif self._ny_maaned == 10:
            self._ny_maaned = str("oktober")
        elif self._ny_maaned == 11:
            self._ny_maaned = str("november")
        else:
            self._ny_maaned = str("desember")
        return self._ny_dag + ".", self._ny_maaned, self._nytt_aar
    def er_det_idag(self, dag_nr):
        return self._ny_dag == dag_nr
    def dato_sjekking(self, dag, måned, år):
        if self._nytt_aar < år:
            return True
        elif self._nytt_aar == år and self._ny_maaned < måned:
            return True
        elif self._nytt_aar == år and self._ny_maaned == måned and self._ny_dag < dag:
            return True
        return False
    
        

