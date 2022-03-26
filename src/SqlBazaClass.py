import sqlite3, sys
from sqlite3 import Error
import atexit
import json
from PyQt5 import QtCore, QtGui, QtWidgets

from ListaDatumaClass import ListaDatuma
from ListaZadatakaClass import ListaZadataka
from ZadatakClass import Zadatak

class SqlBaza(object):
    #Svojstva koja koristimo u klasi
    otvorena_datoteka = None
    up = None
    Baza = None

    #Konstruktor SqlBaza(postojeca, path)
    #Ako postoji otvaramo ju, a ako ne postoji kreiramo novu datoteku s bazom i u nju upisujemo novu tablicu
    def __init__(self, postojeca, path):
        self.otvorena_datoteka = path

        if(postojeca == True):
            self.OtvoriBazu(self.otvorena_datoteka)
        else:
            if(self.otvorena_datoteka[-3:] != ".db"):
                self.otvorena_datoteka += ".db"
            self.OtvoriBazu(self.otvorena_datoteka)
            self.NovaTablica()
        atexit.register(self.Baza.close)

    #Otvara bazu 
    def OtvoriBazu(self, path):
        try:
            self.Baza = sqlite3.connect(path)
        except Error as e:
            print(e)
            QtWidgets.QApplication(sys.argv).closeAllWindows()
            sys.exit(QtWidgets.QApplication(sys.argv).exec_())

    #Kreira novu tablicu naziva DATUMI u bazi 
    def NovaTablica(self):
        self.Baza.execute("DROP TABLE IF EXISTS DATUMI")
        self.Baza.execute("CREATE TABLE DATUMI (datum TEXT PRIMARY KEY, zadaci TEXT)")
        self.Baza.commit()
    
    #Dodajemo datum u bazu
    def BazaDodajDatum(self, datum, vrijednosti):
        zadaci = []
        for i in vrijednosti:
            y = []
            y.append(i.VratiTekst())
            y.append(i.VratiStanje())
            zadaci.append(y)
        self.Baza.execute("INSERT INTO DATUMI VALUES ('{0}','{1}')".format(datum,json.dumps(zadaci)))
        self.Baza.commit()

    #Čuvamo zadatke za određeni datum u bazi
    def BazaSacuvajDatum(self, datum, vrijednosti):
        zadaci = []
        for i in vrijednosti:
            y = []
            y.append(i.VratiTekst())
            y.append(i.VratiStanje())
            zadaci.append(y)
        self.Baza.execute("UPDATE DATUMI set zadaci = '{0}' where datum = '{1}'".format(json.dumps(zadaci),datum))
        self.Baza.commit()

    #Učitavamo sve datume koji se nalaze u bazi
    def BazaUcitajDatume(self):
        _dict = { }
        curs = self.Baza.execute("SELECT * FROM DATUMI")
        for redak in curs:
            temp = ListaZadataka(redak[0])
            x = json.loads(redak[1])
            for i in x:
                temp.DodajZadatak(Zadatak(i[0],i[1]))
            _dict.update({ temp.VratiDatum() : temp })
        return _dict
    
    #Vraća path datoteke u kojoj je spremljena lista
    def VratiPathOtvoreneBaze(self):
        return self.otvorena_datoteka